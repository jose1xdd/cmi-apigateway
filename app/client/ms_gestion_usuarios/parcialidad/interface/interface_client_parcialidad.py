from typing import Dict, Any, Optional
from abc import ABC, abstractmethod


class IClientParcialidad(ABC):

    @abstractmethod
    def create_parcialidad(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        """POST /parcialidad/create"""
        pass

    @abstractmethod
    def update_parcialidad(self, id_parcialidad: str, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        """PUT /parcialidad/{id}"""
        pass

    @abstractmethod
    def delete_parcialidad(self, id_parcialidad: str, headers: Optional[Dict[str, str]] = None):
        """DELETE /parcialidad/{id}"""
        pass

    @abstractmethod
    def get_parcialidad(self, id_parcialidad: str, headers: Optional[Dict[str, str]] = None):
        """GET /parcialidad/{id}"""
        pass

    @abstractmethod
    def list_parcialidades(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None):
        """GET /parcialidad?page=..&page_size=.."""
        pass
