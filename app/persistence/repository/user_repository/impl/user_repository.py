# app/persistence/repository/usuario_repository.py

from app.persistence.model.usuario import Usuario
from app.models.schemas.usuario_schema import UsuarioCreate

from sqlalchemy import select

from app.persistence.repository.base_repository.impl.base_repository import BaseRepository
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository

class UsuarioRepository(BaseRepository[UsuarioCreate, str], IUsuarioRepository):
    def __init__(self):
        super().__init__(Usuario)

    async def get_by_email(self, db, email: str):
        result = await db.execute(select(self.model).where(self.model.email == email))
        return result.scalars().first()
