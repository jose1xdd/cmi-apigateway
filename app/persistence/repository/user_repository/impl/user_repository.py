from sqlalchemy.orm import Session
from typing import Any, Dict, Optional
from app.persistence.model.usuario import Usuario
from app.persistence.repository.base_repository.impl.base_repository import BaseRepository
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository


class UsuarioRepository(BaseRepository, IUsuarioRepository):
    def __init__(self, db: Session):
        super().__init__(Usuario, db)

    def get_by_email(self, email: str) -> Optional[Usuario]:
        return self.db.query(self.model).filter(self.model.email == email).first()

    def update_password(self, email: str, password: str) -> Optional[Usuario]:
        usuario = self.get_by_email(email)
        if usuario:
            usuario.password = password
            self.db.commit()
            self.db.refresh(usuario)
        return usuario

    def get_by_persona_id(self, persona_id: str):
        return self.db.query(self.model).filter(self.model.personaId == persona_id).first()

    def find_all_user(self, page: int, page_size: int, filters: Dict[str, Any]):
        query = (
            self.apply_filters(self.db, Usuario, filters)
        )
        return self.paginate(page, page_size, query)
