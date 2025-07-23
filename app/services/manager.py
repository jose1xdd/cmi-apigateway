import logging

from app.models.inputs.login_input import LoginInput
from app.models.schemas.usuario_schema import UsuarioCreate
from app.persistence.model.usuario import Usuario
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository
from app.services.hashing_service.interface.interface_hashing_service import IHashingService
from app.services.jwt_service.interface.interface_jwt_service import IJwtService
from app.utils.exceptions_handlers.models.error_response import AppException
from fastapi import status

class Manager():
    def __init__(self,
                 jwt_service: IJwtService,
                 hashing_service: IHashingService,
                 usuario_repository: IUsuarioRepository,
                 logger: logging.Logger):
        self.usuario_repository = usuario_repository
        self.logger = logger
        self.jwt_service = jwt_service
        self.hashing_service = hashing_service

    def test(self):
        self.logger.info("123")
        usuario = UsuarioCreate(
            email="juan1.perez@example.com",
            password=self.hashing_service.hash_password("123456789"),
            personaId="123456789",
            rol="admin"
        )
        return self.usuario_repository.create(usuario)

    def login(self, data: LoginInput):
        self.logger.info("se inicia el proceso de loggin")
        hashed_pasword = self.hashing_service.hash_password(data.password)
        user:Usuario = self.usuario_repository.get_by_email(data.email)
        if(not user):
            self.logger.error("usuario no existente")
            raise AppException(mensaje="Usuario no Existente",codigo_http=status.HTTP_400_BAD_REQUEST)
        verify_password = self.hashing_service.verify_password(
            user.password, hashed_pasword)
        if (verify_password):
            self.logger.info("contraseña validada generando jwt")
            jwt = self.jwt_service.create_jwt_token(data.email, user.rol.value)
            return {"estado": "Exitoso", "jwt": jwt}
        return {"estado": "Fallido", "contraseña": "invalida"}
