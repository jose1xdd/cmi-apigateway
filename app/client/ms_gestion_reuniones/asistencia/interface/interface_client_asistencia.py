from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class IClientAsistencia(ABC):

    @abstractmethod
    def assign_asistencia(
        self,
        reunion_id: int,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ):
        """Asigna asistencia a varias personas en una reunión"""
        pass

    @abstractmethod
    def user_assign_asistencia(
        self,
        reunion_id: int,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ):
        """Asigna asistencia de un usuario específico en una reunión"""
        pass

    @abstractmethod
    def delete_asistencia(
        self,
        reunion_id: int,
        persona_id: int,
        headers: Optional[Dict[str, str]] = None
    ):
        """Elimina una asistencia por ID"""
        pass

    @abstractmethod
    def get_personas_with_asistencia(
        self,
        reunion_id: int,
        page: int,
        page_size: int,
        headers: Optional[Dict[str, str]] = None,
        numero_documento: Optional[str] = None,
        nombre: Optional[str] = None,
        apellido: Optional[str] = None
    ):
        pass

    @abstractmethod
    def get_asistencia_persona(self, persona_id: int, reunion_id: int, headers):
        pass
