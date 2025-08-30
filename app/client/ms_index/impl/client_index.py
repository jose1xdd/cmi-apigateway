import requests
from typing import Dict, Any, Optional, List
from requests import Response

from app.client.ms_index.interface.interface_client_index import IClientIndex
from app.utils.constans import JSON_HEADER

class ClientIndex(IClientIndex):
    def __init__(self, url: str):
        self.url = url.rstrip("/")

    def create_publicacion(
        self,
        titulo: str,
        contenido: Optional[str] = None,
        fotos: Optional[List[bytes]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        merged_headers = {**(headers or {})}
        files = []
        if fotos:
            for i, foto in enumerate(fotos):
                files.append(("fotos", ("foto.png", foto, "image/png")))

        data = {
            "titulo": titulo,
            "contenido": contenido
        }
        return requests.post(
            f"{self.url}/index/create",
            data=data,
            files=files if fotos else None,
            headers=merged_headers,
        )

    def agregar_fotos(
        self,
        publicacion_id: int,
        fotos: List[bytes],
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        merged_headers = {**(headers or {})}
        files = []
        for i, foto in enumerate(fotos):
            files.append(("fotos", (f"foto_{i}.png", foto, "image/png")))

        return requests.post(
            f"{self.url}/index/{publicacion_id}/fotos",
            files=files,
            headers=merged_headers,
        )

    def get_all_publicacion(
        self,
        page: int = 1,
        page_size: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        merged_headers = {**JSON_HEADER, **(headers or {})}
        params = {
            "page": page,
            "page_size": page_size,
            **(filters or {})
        }
        return requests.get(f"{self.url}/index", params=params, headers=merged_headers)

    def get_foto_by_id(
        self,
        foto_id: int,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        merged_headers = {**(headers or {})}
        return requests.get(f"{self.url}/index/{foto_id}", headers=merged_headers)

    def update_publicacion(
        self,
        publicacion_id: int,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.put(
            f"{self.url}/index/{publicacion_id}",
            json=body,
            headers=merged_headers,
        )

    def eliminar_foto(
        self,
        foto_id: int,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        merged_headers = {**(headers or {})}
        return requests.delete(f"{self.url}/index/foto/{foto_id}", headers=merged_headers)

    def eliminar_publicacion(
        self,
        publicacion_id: int,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response:
        merged_headers = {**(headers or {})}
        return requests.delete(f"{self.url}/index/{publicacion_id}", headers=merged_headers)
