from abc import abstractmethod
from app.persistence.model.codigo_recuperacion import CodigoRecuperacion
from app.persistence.repository.base_repository.interface.ibase_repository import IBaseRepository
from typing import Optional


class IRecoveryCodeRepository(IBaseRepository[CodigoRecuperacion, int]):
    @abstractmethod
    def get_by_email_and_code(self, email: str, code: str) -> Optional[CodigoRecuperacion]:
        pass
