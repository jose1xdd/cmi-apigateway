import requests
from typing import Dict, Any, Optional

from app.client.ms_gestion_usuarios.familia.interface.interface_client_familia import IClientFamilia
from app.utils.constans import JSON_HEADER


class ClientFamilia(IClientFamilia):
    def __init__(self, url: str):
        self.url = url.rstrip("/")

    def create_familia(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.post(f"{self.url}/familias/create", json=body, headers=merged_headers)

    def delete_familia(self, id_familia: int, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.delete(f"{self.url}/familias/{id_familia}", headers=merged_headers)

    def list_familias(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        params = {
            "page": page,
            "page_size": page_size
        }
        return requests.get(f"{self.url}/familias", params=params, headers=merged_headers)
