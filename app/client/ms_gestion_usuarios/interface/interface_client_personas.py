from abc import ABC, abstractmethod
from typing import Dict, Any


class IClientPersonas(ABC):
    @abstractmethod
    def create_persona(self, body: Dict[str, Any]):
        pass

    @abstractmethod
    def update_persona(self, id_persona: str, body: Dict[str, Any]):
        pass

    @abstractmethod
    def delete_persona(self, id_persona: str):
        pass

    @abstractmethod
    def list_personas(self, page: int = 1, page_size: int = 10):
        pass
