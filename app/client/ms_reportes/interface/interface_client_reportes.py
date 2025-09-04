from abc import ABC, abstractmethod
from typing import Dict, Optional


class IClientReportes(ABC):
    @abstractmethod
    def get_reporte_personas(self, headers: Optional[Dict[str, str]] = None):
        pass
