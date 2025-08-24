import requests
from typing import Dict, Any, Optional

from app.client.ms_gestion_usuarios.parcialidad.interface.interface_client_parcialidad import IClientParcialidad
from app.utils.constans import JSON_HEADER


class ClientParcialidad(IClientParcialidad):
    def __init__(self, url: str):
        # Quita el "/" final si lo tiene para evitar errores en concatenación
        self.url = url.rstrip("/")

    def create_parcialidad(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        """POST /parcialidad/create"""
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.post(f"{self.url}/parcialidad/create", json=body, headers=merged_headers)

    def update_parcialidad(self, id_parcialidad: str, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        """PUT /parcialidad/{id}"""
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.put(f"{self.url}/parcialidad/{id_parcialidad}", json=body, headers=merged_headers)

    def delete_parcialidad(self, id_parcialidad: str, headers: Optional[Dict[str, str]] = None):
        """DELETE /parcialidad/{id}"""
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.delete(f"{self.url}/parcialidad/{id_parcialidad}", headers=merged_headers)

    def get_parcialidad(self, id_parcialidad: str, headers: Optional[Dict[str, str]] = None):
        """GET /parcialidad/{id}"""
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(f"{self.url}/parcialidad/{id_parcialidad}", headers=merged_headers)

    def list_parcialidades(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None, filters: Optional[Dict[str, Any]] = None):
        """GET /parcialidad?page=..&page_size=.."""
        merged_headers = {**JSON_HEADER, **(headers or {})}
        params = {
            "page": page,
            "page_size": page_size
        }
        params = params | filters
        return requests.get(f"{self.url}/parcialidad", params=params, headers=merged_headers)
