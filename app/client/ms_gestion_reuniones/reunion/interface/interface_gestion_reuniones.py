from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class IClientReunion(ABC):
    """
    Interfaz para el cliente HTTP que gestiona las peticiones
    hacia el microservicio de reuniones.
    """

    @abstractmethod
    def create_reunion(
        self,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ):
        """Crea una nueva reunión."""
        pass

    @abstractmethod
    def get_reunion(
        self,
        reunion_id: int,
        headers: Optional[Dict[str, str]] = None
    ):
        """Obtiene una reunión por su ID."""
        pass

    @abstractmethod
    def list_reuniones(
        self,
        page: int,
        page_size: int,
        filters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ):
        """Lista las reuniones registradas con filtros opcionales."""
        pass

    @abstractmethod
    def update_reunion(
        self,
        reunion_id: int,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ):
        """Actualiza los datos de una reunión existente."""
        pass

    @abstractmethod
    def delete_reunion(
        self,
        reunion_id: int,
        headers: Optional[Dict[str, str]] = None
    ):
        """Elimina una reunión existente."""
        pass

    @abstractmethod
    def abrir_reunion(
        self,
        reunion_id: int,
        headers: Optional[Dict[str, str]] = None
    ):
        """Abre una reunión (PROGRAMADA → EN_CURSO)."""
        pass

    @abstractmethod
    def cerrar_reunion(
        self,
        reunion_id: int,
        headers: Optional[Dict[str, str]] = None
    ):
        """Cierra una reunión (EN_CURSO → CERRADA)."""
        pass
