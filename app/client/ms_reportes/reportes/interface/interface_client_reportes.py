from abc import ABC, abstractmethod
from typing import Dict, Optional


class IClientReportes(ABC):
    @abstractmethod
    def get_reporte_personas(self, headers: Optional[Dict[str, str]] = None):
        pass

    @abstractmethod
    def get_reporte_asistencia(self, reunion_id: int, headers: Optional[Dict[str, str]] = None):
        pass

    @abstractmethod
    def get_reporte_familia(self, familia_id: int, headers: Optional[Dict[str, str]] = None):
        pass

    @abstractmethod
    def get_resumen_dashboard(self, headers: Optional[Dict[str, str]] = None):
        pass
