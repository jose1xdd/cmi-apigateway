import logging

from dependency_injector.wiring import inject
from app.models.inputs.login_input import LoginInput
from app.models.schemas.usuario_schema import UsuarioCreate
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository
from app.services.hashing_service.interface.interface_hashing_service import IHashingService
from app.services.jwt_service.interface.interface_jwt_service import IJwtService


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
            password="secreto123",
            personaId="1234567890"
        )
        return self.usuario_repository.create(usuario)

    def login(self, data: LoginInput):

        self.logger.info(
            f"el hashing es {self.hashing_service.hash_password(data.email)}")
        self.logger.info(f"jwt generado : {self.jwt_service.create_jwt_token(data.email)}")
