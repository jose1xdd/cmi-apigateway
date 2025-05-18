# app/persistence/repository/interfaces/iusuario_repository.py

from app.models.schemas.usuario_schema import UsuarioCreate
from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository

class IUsuarioRepository(IBaseRepository[UsuarioCreate, str]):
    async def get_by_email(self, db, email: str):
        raise NotImplementedError
