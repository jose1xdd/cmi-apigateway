from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class IClientPersonas(ABC):

    @abstractmethod
    def create_persona(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        pass

    @abstractmethod
    def update_persona(self, id_persona: str, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        pass

    @abstractmethod
    def delete_persona(self, id_persona: str, headers: Optional[Dict[str, str]] = None):
        pass

    @abstractmethod
    def list_personas(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None):
        pass

    @abstractmethod
    def assing_familia(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        pass

    @abstractmethod
    def get_persona(self, id_persona: str, headers: Optional[Dict[str, str]] = None):
        pass
