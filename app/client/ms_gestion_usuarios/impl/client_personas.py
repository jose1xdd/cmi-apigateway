import requests
from typing import Dict, Any

from app.client.ms_gestion_usuarios.interface.interface_client_personas import IClientPersonas


class ClientPersonas(IClientPersonas):
    def __init__(self, url: str):
        self.url = url.rstrip("/")

    def create_persona(self, body: Dict[str, Any]):
        headers = {
            "Content-Type": "application/json"
        }
        return requests.post(f"{self.url}/personas/create", json=body, headers=headers)

    def update_persona(self, id_persona: str, body: Dict[str, Any]):
        headers = {
            "Content-Type": "application/json"
        }
        return requests.put(f"{self.url}/personas/{id_persona}", json=body, headers=headers)

    def delete_persona(self, id_persona: str):
        return requests.delete(f"{self.url}/personas/{id_persona}")

    def list_personas(self, page: int = 1, page_size: int = 10):
        params = {
            "page": page,
            "page_size": page_size
        }
        return requests.get(f"{self.url}/personas", params=params)
