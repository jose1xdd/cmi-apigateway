from abc import abstractmethod
from app.models.schemas.usuario_schema import UsuarioCreate
from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository
from typing import Optional


class IUsuarioRepository(IBaseRepository[UsuarioCreate, int]):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional[UsuarioCreate]:
        pass

    @abstractmethod
    def update_password(self, email: str, password: str):
        pass
