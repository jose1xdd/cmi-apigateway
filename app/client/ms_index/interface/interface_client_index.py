from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from requests import Response


class IClientIndex(ABC):

    @abstractmethod
    def create_publicacion(
        self,
        titulo: str,
        contenido: Optional[str] = None,
        fotos: Optional[List[bytes]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        pass

    @abstractmethod
    def agregar_fotos(
        self,
        publicacion_id: int,
        fotos: List[bytes],
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        pass

    @abstractmethod
    def get_all_publicacion(
        self,
        page: int = 1,
        page_size: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        pass

    @abstractmethod
    def get_foto_by_id(
        self,
        foto_id: int,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        pass

    @abstractmethod
    def update_publicacion(
        self,
        publicacion_id: int,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        pass

    @abstractmethod
    def eliminar_foto(
        self,
        foto_id: int,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        pass

    @abstractmethod
    def eliminar_publicacion(
        self,
        publicacion_id: int,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        pass
