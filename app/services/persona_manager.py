import logging
from typing import Any, Dict

from fastapi import UploadFile

from app.client.ms_gestion_usuarios.personas.interface.interface_client_personas import IClientPersonas


class PersonaManager():
    def __init__(self,
                 client_personas: IClientPersonas,
                 logger: logging.Logger):
        self.client_personas = client_personas
        self.logger = logger

    def create_person(self, data, headers):
        return self.client_personas.create_persona(data, headers)

    def update_person(self, id_persona: str, data, headers):
        return self.client_personas.update_persona(id_persona, data, headers)

    def delete_person(self, id_persona: str, headers):
        return self.client_personas.delete_persona(id_persona, headers)

    def list_personas(self, page: int, page_size: int, headers, filters: Dict[str, Any]):
        return self.client_personas.list_personas(page=page, page_size=page_size, headers=headers, filters=filters)

    def assing_familia(self, data, headers):
        return self.client_personas.assing_familia(data, headers)

    def get_persona(self, id_persona: str, headers):
        return self.client_personas.get_persona(id_persona, headers)

    async def upload_excel(self, file: UploadFile, headers):
        file_bytes = await file.read()  # 👈 lee el contenido en memoria
        return self.client_personas.upload_excel(file.filename, file_bytes, headers)
    
    def register_defuncion(self, data, headers):
        return self.client_personas.register_defuncion(data, headers)

