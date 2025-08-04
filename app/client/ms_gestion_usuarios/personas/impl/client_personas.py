import requests
from typing import Dict, Any, Optional

from app.client.ms_gestion_usuarios.personas.interface.interface_client_personas import IClientPersonas
from app.utils.constans import JSON_HEADER


class ClientPersonas(IClientPersonas):
    def __init__(self, url: str):
        self.url = url.rstrip("/")

    def create_persona(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.post(f"{self.url}/personas/create", json=body, headers=merged_headers)

    def update_persona(self, id_persona: str, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.put(f"{self.url}/personas/{id_persona}", json=body, headers=merged_headers)

    def delete_persona(self, id_persona: str, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.delete(f"{self.url}/personas/{id_persona}", headers=merged_headers)

    def list_personas(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        params = {
            "page": page,
            "page_size": page_size
        }
        return requests.get(f"{self.url}/personas", params=params, headers=merged_headers)
