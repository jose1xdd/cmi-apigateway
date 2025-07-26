from abc import ABC, abstractmethod
from typing import Dict


class IClientPersonas(ABC):
    @abstractmethod
    def create_persona(self, body: Dict):
        pass
