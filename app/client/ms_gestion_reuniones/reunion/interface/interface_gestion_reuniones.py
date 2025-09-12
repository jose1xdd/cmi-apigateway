from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class IClientReunion(ABC):
    @abstractmethod
    def create_reunion(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        """Crea una nueva reunión"""
        pass

    @abstractmethod
    def get_reunion(self, reunion_id: int, headers: Optional[Dict[str, str]] = None):
        """Obtiene una reunión por su ID"""
        pass

    @abstractmethod
    def list_reuniones(
        self,
        page: int = 1,
        page_size: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ):
        """Lista reuniones con soporte de paginación y filtros"""
        pass

    @abstractmethod
    def update_reunion(self, reunion_id: int, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        """Actualiza una reunión existente"""
        pass

    @abstractmethod
    def delete_reunion(self, reunion_id: int, headers: Optional[Dict[str, str]] = None):
        """Elimina una reunión por su ID"""
        pass

    @abstractmethod
    def generate_reunion_code(self, reunion_id: int, headers: Optional[Dict[str, str]] = None):
        pass
