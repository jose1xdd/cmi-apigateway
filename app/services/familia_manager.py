import logging
from typing import Dict, Any, Optional
from fastapi import UploadFile
from app.client.ms_gestion_usuarios.familia.interface.interface_client_familia import IClientFamilia


class FamiliaManager:
    def __init__(self, client: IClientFamilia, logger: logging.Logger):
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

    def search_familias(
        self,
        query: str,
        page: int = 1,
        page_size: int = 10,
        parcialidad_id: int | None = None,
        rango_miembros: str | None = None,
        estado: str | None = None,
        headers: Optional[Dict[str, str]] = None
    ):
        self.logger.info(
            f"Buscando familias con criterio: {query}, "
            f"parcialidad_id={parcialidad_id}, rango_miembros={rango_miembros}, estado={estado}"
        )
        return self.client.search_familias(
            query=query,
            page=page,
            page_size=page_size,
            parcialidad_id=parcialidad_id,
            rango_miembros=rango_miembros,
            estado=estado,
            headers=headers
        )

    def get_familias_leaderdata(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None):
        self.logger.info(
            "Obteniendo datos de familias con líder y parcialidad")
        return self.client.get_familias_leaderdata(page, page_size, headers)

    def get_miembros_familia(self, id_familia: int, page: int = 1, page_size: int = 10, query: Optional[str] = None, headers: Optional[Dict[str, str]] = None):
        self.logger.info(f"Obteniendo miembros de la familia {id_familia}")
        return self.client.get_miembros_familia(id_familia, page, page_size, query, headers)

    def get_familia_resumen(self, id_familia: int, headers: Optional[Dict[str, str]] = None):
        self.logger.info(f"Obteniendo resumen de la familia {id_familia}")
        return self.client.get_familia_resumen(id_familia, headers)

    def get_estadisticas_generales(self, headers: Optional[Dict[str, str]] = None):
        self.logger.info("Consultando estadísticas generales")
        return self.client.get_estadisticas_generales(headers)

    def get_familia(self, id_familia: int, headers: Optional[Dict[str, str]] = None):
        self.logger.info(f"Obteniendo familia con ID: {id_familia}")
        return self.client.get_familia(id_familia, headers)

    async def upload_excel(self, file: UploadFile, headers):
        file_bytes = await file.read()
        return self.client.upload_excel(file.filename, file_bytes, headers)

    def update_familia(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        self.logger.info(f"Actualizando familia con datos: {body}")
        return self.client.update_familia(body, headers)
