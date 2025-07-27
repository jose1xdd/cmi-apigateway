from typing import Optional
from sqlalchemy.orm import Session
from app.persistence.model.codigo_recuperacion import CodigoRecuperacion
from app.persistence.repository.base_repository.impl.base_repository import BaseRepository
from app.persistence.repository.recovery_code_repository.interface.interface_recovery_code_repository import IRecoveryCodeRepository


class RecoveryCodeRepository(BaseRepository,IRecoveryCodeRepository):
    def __init__(self, db: Session):
        # Llamar al constructor de la clase base
        super().__init__(CodigoRecuperacion, db)

    def get_by_email_and_code(self, email: str, code: str) -> Optional[CodigoRecuperacion]:
        return (
            self.db.query(CodigoRecuperacion)
            .filter(CodigoRecuperacion.emailUsuario == email)
            .filter(CodigoRecuperacion.codigo == code)
            .filter(CodigoRecuperacion.estado == True)
            .first()
        )
