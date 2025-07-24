from typing import Type, TypeVar
from sqlalchemy.orm import Session
from app.persistence.repository.recovery_code_repository.impl.recovery_code_repository import RecoveryCodeRepository
from app.persistence.repository.recovery_code_repository.interface.interface_recovery_code_repository import IRecoveryCodeRepository
from app.persistence.repository.user_repository.impl.user_repository import UsuarioRepository
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository

T = TypeVar("T")


class RepositoryFactory:

    def __init__(self, db: Session):
        self.db = db

    _registry: dict[Type, Type] = {
        IUsuarioRepository: UsuarioRepository,
        IRecoveryCodeRepository: RecoveryCodeRepository
    }

    def get_repository(self, interface: Type[T]) -> T:
        impl_class = self._registry.get(interface)
        if not impl_class:
            raise ValueError(
                f"No hay implementación registrada para la interfaz: {interface}")
        # Solo pasamos db, el modelo se define en el repositorio
        return impl_class(self.db)
