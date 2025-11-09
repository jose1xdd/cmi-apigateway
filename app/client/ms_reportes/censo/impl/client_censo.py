from typing import Dict, Optional

import requests
from app.client.ms_reportes.censo.interface.inteface_client_censo import IClientCenso
from app.utils.constans import JSON_HEADER


class ClientCenso(IClientCenso):
    def __init__(self, url: str):
        self.url = url.rstrip("/")

    def generar_censo(self, payload: dict, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.post(f"{self.url}/generar", json=payload, headers=merged_headers)

    def listar_procesos(self, params: dict, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(f"{self.url}/procesos", params=params, headers=merged_headers)

    def exportar_censo(self, censo_proceso_id: int, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(f"{self.url}/exportar/{censo_proceso_id}", headers=merged_headers, stream=True)