from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import requests


class IClientFamilia(ABC):

    @abstractmethod
    def create_familia(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """Crea una familia."""
        pass

    @abstractmethod
    def delete_familia(self, id_familia: int, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """Elimina una familia por ID."""
        pass

    @abstractmethod
    def list_familias(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None) -> requests.Response:
        """Obtiene una lista paginada de familias."""
        pass
