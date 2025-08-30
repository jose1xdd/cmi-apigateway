import logging
from typing import Dict, Any, Optional, List
from requests import Response

from app.client.ms_index.interface.interface_client_index import IClientIndex


class IndexManager:
    def __init__(self, client: IClientIndex, logger: logging.Logger):
        self.client = client
        self.logger = logger

    def create_publicacion(
        self,
        body: Dict[str, Any],
        fotos: Optional[List[bytes]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        self.logger.info(f"Creando publicación con datos: {body}")
        return self.client.create_publicacion(
            titulo=body.get("titulo"),
            contenido=body.get("contenido"),
            fotos=fotos,
            headers=headers,
        )

    def agregar_fotos(
        self,
        publicacion_id: int,
        fotos: List[bytes],
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        self.logger.info(f"Agregando fotos a publicación ID {publicacion_id}")
        return self.client.agregar_fotos(publicacion_id, fotos, headers)

    def get_all_publicacion(
        self,
        page: int,
        page_size: int,
        filters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        self.logger.info(
            f"Consultando publicaciones page={page}, size={page_size}, filters={filters}")
        return self.client.get_all_publicacion(page, page_size, filters, headers)

    def get_foto_by_id(self, foto_id: int, headers: Optional[Dict[str, str]] = None) -> Response:
        self.logger.info(f"Obteniendo foto ID {foto_id}")
        return self.client.get_foto_by_id(foto_id, headers)

    def update_publicacion(
        self,
        publicacion_id: int,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        self.logger.info(
            f"Actualizando publicación ID {publicacion_id} con body: {body}")
        return self.client.update_publicacion(publicacion_id, body, headers)

    def eliminar_foto(self, foto_id: int, headers: Optional[Dict[str, str]] = None) -> Response:
        self.logger.info(f"Eliminando foto ID {foto_id}")
        return self.client.eliminar_foto(foto_id, headers)

    def eliminar_publicacion(self, publicacion_id: int, headers: Optional[Dict[str, str]] = None) -> Response:
        self.logger.info(
            f"Eliminando publicación ID {publicacion_id} y sus fotos")
        return self.client.eliminar_publicacion(publicacion_id, headers)
