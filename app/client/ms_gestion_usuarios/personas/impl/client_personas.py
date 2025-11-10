import requests
from typing import BinaryIO, Dict, Any, Optional

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

    def list_personas(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None, filters: Optional[Dict[str, Any]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        params = {
            "page": page,
            "page_size": page_size
        }
        params = params | filters
        return requests.get(f"{self.url}/personas", params=params, headers=merged_headers)

    def assing_familia(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.patch(f"{self.url}/personas/assing-family", json=body, headers=merged_headers)

    def get_persona(self, id_persona: str, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(f"{self.url}/personas/{id_persona}", headers=merged_headers)

    def upload_excel(self, filename: str, file_bytes: bytes, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**(headers or {})}
        files = {"file": (filename, file_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
        return requests.post(f"{self.url}/personas/upload-excel", files=files, headers=merged_headers)
    
    def register_defuncion(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.patch(f"{self.url}/personas/register-defuncion", json=body, headers=merged_headers)
