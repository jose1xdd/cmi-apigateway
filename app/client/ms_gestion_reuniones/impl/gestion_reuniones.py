import requests
from typing import Dict, Any, Optional

from app.client.ms_gestion_reuniones.interface.interface_gestion_reuniones import IClientReunion
from app.utils.constans import JSON_HEADER


class ClientReunion(IClientReunion):
    def __init__(self, url: str):
        self.url = url.rstrip("/")

    def create_reunion(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.post(f"{self.url}/reunion/create", json=body, headers=merged_headers)

    def get_reunion(self, reunion_id: int, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(f"{self.url}/reunion/{reunion_id}", headers=merged_headers)

    def list_reuniones(
        self,
        page: int = 1,
        page_size: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        params = {
            "page": page,
            "page_size": page_size
        }
        if filters:
            params.update(filters)
        return requests.get(f"{self.url}/reunion/", params=params, headers=merged_headers)

    def update_reunion(self, reunion_id: int, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.put(f"{self.url}/reunion/{reunion_id}", json=body, headers=merged_headers)

    def delete_reunion(self, reunion_id: int, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.delete(f"{self.url}/reunion/{reunion_id}", headers=merged_headers)
