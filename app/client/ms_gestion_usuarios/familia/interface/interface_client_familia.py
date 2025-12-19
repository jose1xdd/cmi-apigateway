from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class IClientFamilia(ABC):
    """
    Interfaz del cliente HTTP para consumir el microservicio de gestión de Familias.
    Define los métodos que deben ser implementados por ClientFamilia.
    """

    @abstractmethod
    def create_familia(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        """Crea una nueva familia."""
        pass

    @abstractmethod
    def delete_familia(self, id_familia: int, headers: Optional[Dict[str, str]] = None):
        """Elimina una familia por ID."""
        pass

    @abstractmethod
    def list_familias(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None):
        """Obtiene la lista paginada de familias."""
        pass

    @abstractmethod
    def search_familias(
        self,
        query: str,
        page: int = 1,
        page_size: int = 10,
        parcialidad_id: int | None = None,
        rango_miembros: str | None = None,
        estado: str | None = None,
        headers: Optional[Dict[str, str]] = None
    ):
        pass

    @abstractmethod
    def get_familias_leaderdata(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None):
        """Obtiene familias con datos del líder y su parcialidad."""
        pass

    @abstractmethod
    def get_miembros_familia(
        self,
        id_familia: int,
        page: int = 1,
        page_size: int = 10,
        query: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        vivos: Optional[bool] = False
        
    ):
        """Obtiene los miembros de una familia, con filtro opcional."""
        pass

    @abstractmethod
    def get_familia_resumen(self, id_familia: int, headers: Optional[Dict[str, str]] = None):
        """Obtiene el resumen de una familia (líder, parcialidad, miembros, etc.)."""
        pass

    @abstractmethod
    def get_estadisticas_generales(self, headers: Optional[Dict[str, str]] = None):
        """Obtiene las estadísticas globales del sistema (familias, personas, etc.)."""
        pass

    @abstractmethod
    def get_familia(self, id_familia: int, headers: Optional[Dict[str, str]] = None):
        """Obtiene una familia por su ID."""
        pass

    @abstractmethod
    def upload_excel(self, filename: str, file_bytes: bytes, headers: Optional[Dict[str, str]] = None):
        """Carga masiva de familias desde un archivo Excel."""
        pass

    @abstractmethod
    def update_familia(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        pass
