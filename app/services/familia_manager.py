import logging
from typing import Dict, Any, Optional

from fastapi import UploadFile

from app.client.ms_gestion_usuarios.familia.interface.interface_client_familia import IClientFamilia


class FamiliaManager:
    def __init__(self, client: IClientFamilia, logger: logging.getLogger):
        self.client = client
        self.logger = logger

    def create_familia(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        self.logger.info(f"Creando familia con datos: {body}")
        return self.client.create_familia(body, headers)

    def delete_familia(self, id_familia: int, headers: Optional[Dict[str, str]] = None):
        self.logger.info(f"Eliminando familia con ID: {id_familia}")
        return self.client.delete_familia(id_familia, headers)

    def list_familias(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None):
        self.logger.info(
            f"Listando familias - Página: {page}, Tamaño: {page_size}")
        return self.client.list_familias(page, page_size, headers)

    def get_familia(self, familia_id: int, headers: Optional[Dict[str, str]] = None):
        return self.client.get_familia(familia_id, headers)

    async def upload_excel(self, file: UploadFile, headers):
        file_bytes = await file.read()  # 👈 lee el contenido en memoria
        return self.client.upload_excel(file.filename, file_bytes, headers)
