import requests
from ast import Dict
from app.client.ms_gestion_usuarios.interface.interface_client_personas import IClientPersonas


class ClientPersonas(IClientPersonas):
    def __init__(self, url: str):
        self.url = url

    def create_persona(self, body: Dict):
        headers = {
            "Content-Type": "application/json"
        }
        return requests.post(self.url, json=body, headers=headers)
