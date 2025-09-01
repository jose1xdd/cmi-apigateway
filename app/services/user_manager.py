import logging

from app.models.inputs.usuario.login_input import LoginInput
from app.models.inputs.usuario.recovery_password_input import RecoveryPassword
from app.models.inputs.usuario.reste_password_input import ResetPassword
from app.models.inputs.usuario.user_create import UsuarioCreate
from app.models.inputs.usuario.user_update import UsuarioUpdate
from app.models.outputs.response_estado import EstadoResponse
from app.persistence.model.codigo_recuperacion import CodigoRecuperacion
from app.persistence.model.usuario import Usuario
from app.persistence.repository.persona_repository.interface.interface_persona_repository import IPersonaRepository
from app.persistence.repository.recovery_code_repository.interface.interface_recovery_code_repository import IRecoveryCodeRepository
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository
from app.services.email_service.interface.interface_email_service import IEmailService
from app.services.hashing_service.interface.interface_hashing_service import IHashingService
from app.services.jwt_service.interface.interface_jwt_service import IJwtService
from app.utils.exceptions_handlers.models.error_response import AppException
from fastapi import status

from app.utils.util_functions import generate_recovery_code, generate_temporary_password


class UserManager():
    def __init__(self,
                 jwt_service: IJwtService,
                 hashing_service: IHashingService,
                 usuario_repository: IUsuarioRepository,
                 email_service: IEmailService,
                 code_repository: IRecoveryCodeRepository,
                 persona_repository: IPersonaRepository,
                 logger: logging.Logger):
        self.usuario_repository = usuario_repository
        self.persona_repository = persona_repository
        self.logger = logger
        self.jwt_service = jwt_service
        self.hashing_service = hashing_service
        self.email_service = email_service
        self.code_repository = code_repository

    def login(self, data: LoginInput):
        self.logger.info("se inicia el proceso de loggin")
        hashed_pasword = self.hashing_service.hash_password(data.password)
        user: Usuario = self.usuario_repository.get_by_email(data.email)
        if (not user):
            self.logger.error("usuario no existente")
            raise AppException(mensaje="Usuario no Existente",
                               codigo_http=status.HTTP_400_BAD_REQUEST)
        verify_password = self.hashing_service.verify_password(
            user.password, hashed_pasword)
        if (verify_password):
            self.logger.info("contraseña validada generando jwt")
            jwt = self.jwt_service.create_jwt_token(
                data.email, user.rol.value, user.personaId)
            refresh_token = self.jwt_service.create_refresh_token(
                data.email, user.personaId, user.rol.value)
            return {"estado": "Exitoso", "jwt": jwt, "refresh_token": refresh_token}
        return {"estado": "Fallido", "contraseña": "invalida"}

    def refresh_token(self, refresh_token: str):
        jwt = self.jwt_service.refresh_access_token(refresh_token)
        return {"estado": "Exitoso", "jwt": jwt}

    def password_recovery(self, data: RecoveryPassword):
        self.logger.info(
            "se inicia el proceso para generacion de codigo para contraseña")
        code: str = generate_recovery_code()
        hash_code = self.hashing_service.hash_password(code)
        user_exist = self.usuario_repository.get_by_email(data.email)
        if not user_exist:
            self.logger.error("resteo de contraseña a Usuario inexistente")
            raise AppException(mensaje="Usuario Inexistente para Realizar el Proceso",
                               codigo_http=status.HTTP_400_BAD_REQUEST)
        self.logger.info("se valida existencia del usuario")

        self.code_repository.create(
            CodigoRecuperacion(
                codigo=hash_code, emailUsuario=data.email, estado=True)
        )
        self.logger.info("codigo de recuperacion creado")

        self.email_service.send_email_recovery_password(data.email, code)
        self.logger.info("correo enviado")

    def password_reset(self, data: ResetPassword):
        self.logger.info("se inicia el proceso para resteo de contraseña")
        hashed_code = self.hashing_service.hash_password(data.code)
        code: CodigoRecuperacion = self.code_repository.get_by_email_and_code(
            data.email, hashed_code)
        if not code:
            self.logger.error("Codigo de Reseteo de contraseña inexistente")
            raise AppException(mensaje="Codigo de Reseteo de contraseña inexistente",
                               codigo_http=status.HTTP_400_BAD_REQUEST)
        code.estado = False
        self.code_repository.update(code.id, code)
        password = generate_temporary_password()
        hashed_password = self.hashing_service.hash_password(password)
        self.usuario_repository.update_password(data.email, hashed_password)
        self.email_service.send_email_reset_password(data.email, password)

    def create_user(self, data: UsuarioCreate) -> EstadoResponse:
        self.logger.info(
            f"Iniciando creación de usuario con email: {data.email}")

        persona = self.persona_repository.get(data.personaId)
        if persona is None:
            self.logger.error(f"No existe persona con ID: {data.personaId}")
            raise AppException("Persona a la cual crear usuario no existe")

        user = self.usuario_repository.get_by_persona_id(data.personaId)
        if user is not None:
            self.logger.error(
                f"La persona con ID {data.personaId} ya tiene un usuario asignado")
            raise AppException("Esa persona ya tiene un usuario asignado")

        email_used = self.usuario_repository.get_by_email(data.email)
        if email_used is not None:
            self.logger.error(f"El email {data.email} ya está registrado")
            raise AppException("El email ya se encuentra registrado")
        data.password = self.hashing_service.hash_password(data.password)
        self.usuario_repository.create(data)
        self.logger.info(
            f"Usuario creado exitosamente con email: {data.email}")

        return EstadoResponse(estado="Exitoso", message="Usuario creado exitosamente")

    def delete_user(self, email: str) -> EstadoResponse:
        self.logger.info(
            f"Iniciando eliminación de usuario con email: {email}")

        user = self.usuario_repository.get_by_email(email)
        if user is None:
            self.logger.error(f"No se encontró usuario con email: {email}")
            raise AppException("Usuario no encontrado")

        self.usuario_repository.delete(email)
        self.logger.info(f"Usuario con email {email} eliminado exitosamente")

        return EstadoResponse(estado="Exitoso", message="Usuario eliminado exitosamente")

    def get_user_filter(self, page: int, page_size: int, filters):
        return self.usuario_repository.find_all_user(page, page_size, filters)

    def get_user_by_email(self, email: str):
        return self.usuario_repository.get_by_email(email)

    def update_user(self, email: str, data: UsuarioUpdate):
        user = self.usuario_repository.get_by_email(email)
        if user is None:
            raise AppException("Usuario a actualizar no existe")
        email = self.usuario_repository.get_by_email(data.email)
        if email is not None:
            raise AppException("El email a cambiar ya esta usado")
        self.usuario_repository.update(email, data)
        return EstadoResponse(estado="Exitoso", message="Usuario actualizado")
