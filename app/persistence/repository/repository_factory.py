
from ast import Dict
from typing import Type, TypeVar

from app.persistence.repository.user_repository.impl.user_repository import UsuarioRepository
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository


T = TypeVar("T")


class RepositoryFactory:
    _registry: dict[Type, Type] = {
        IUsuarioRepository: UsuarioRepository,
    }

    @classmethod
    def get_repository(cls, interface: Type[T]) -> T:
        impl_class = cls._registry.get(interface)
        if not impl_class:
            raise ValueError(
                f"No hay implementación registrada para la interfaz: {interface}")
        return impl_class()
