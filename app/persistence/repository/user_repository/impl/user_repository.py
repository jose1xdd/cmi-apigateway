from sqlalchemy.orm import Session
from app.persistence.model.usuario import Usuario
from app.persistence.repository.base_repository.impl.base_repository import BaseRepository


class UsuarioRepository(BaseRepository):
    def __init__(self, db: Session):
        # Llamar al constructor de la clase base
        super().__init__(Usuario, db)

    def get_by_email(self, email: str):
        return self.db.query(self.model).filter(self.model.email == email).first()

    def update_password(self, email: str, password: str):
        usuario = self.get_by_email(email)
        usuario.password = password
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario
