import requests
from typing import Dict, Optional
from app.client.ms_reportes.interface.interface_client_reportes import IClientReportes
from app.utils.constans import JSON_HEADER


class ClientReportes(IClientReportes):
    def __init__(self, url: str):
        self.url = url.rstrip("/")

    def get_reporte_personas(self, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(
            f"{self.url}/reporte/persona",
            headers=merged_headers,
            stream=True
        )

    def get_reporte_asistencia(self, reunion_id: int, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(
            f"{self.url}/reporte/asistencia/{reunion_id}",
            headers=merged_headers,
            stream=True
        )
