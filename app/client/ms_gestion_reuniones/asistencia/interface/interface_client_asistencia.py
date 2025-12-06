from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class IClientAsistencia(ABC):
    """
    Interfaz para el cliente HTTP que gestiona las peticiones hacia
    el microservicio de asistencia.
    """

    @abstractmethod
    def assign_asistencia(
        self,
        reunion_id: int,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ):
        """Asigna asistencia a una persona en una reunión."""
        pass

    @abstractmethod
    def user_assign_asistencia(
        self,
        reunion_id: int,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ):
        """Permite que un usuario registre su propia asistencia usando su número de documento."""
        pass

    @abstractmethod
    def delete_asistencia(
        self,
        reunion_id: int,
        persona_id: int,
        headers: Optional[Dict[str, str]] = None
    ):
        """Elimina una asistencia registrada."""
        pass

    @abstractmethod
    def get_personas_with_asistencia(
        self,
        reunion_id: int,
        page: int,
        page_size: int,
        headers: Optional[Dict[str, str]] = None,
        query: Optional[str] = None,
    ):
        """Obtiene una lista paginada de personas con su estado de asistencia."""
        pass

    @abstractmethod
    def get_asistencia_persona(
        self,
        persona_id: int,
        reunion_id: int,
        headers: Optional[Dict[str, str]] = None
    ):
        """Obtiene el estado de asistencia de una persona específica."""
        pass
