import logging

from dependency_injector.wiring import inject
from app.models.schemas.usuario_schema import UsuarioCreate
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository


class Manager():
    def __init__(self, usuario_repository: IUsuarioRepository, logger: logging.Logger):
        self.usuario_repository = usuario_repository
        self.logger = logger

    def test(self):
        self.logger.info("123")
        usuario = UsuarioCreate(
            email="juan1.perez@example.com",
            password="secreto123",
            personaId="1234567890"
        )
        return self.usuario_repository.create(usuario)
