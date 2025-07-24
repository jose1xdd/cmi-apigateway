from abc import abstractmethod
from app.models.schemas.recovery_code_schema import CodigoRecuperacionCreate
from app.persistence.model.codigo_recuperacion import CodigoRecuperacion
from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository
from typing import Optional


class IRecoveryCodeRepository(IBaseRepository[CodigoRecuperacionCreate, int]):
    @abstractmethod
    def get_by_email_and_code(self, email: str, code: str) -> Optional[CodigoRecuperacion]:
        pass
