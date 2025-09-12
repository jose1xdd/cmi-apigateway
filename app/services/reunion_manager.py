import logging
from typing import Any, Dict

from app.client.ms_gestion_reuniones.reunion.interface.interface_gestion_reuniones import IClientReunion



class ReunionManager:
    def __init__(self, client_reunion: IClientReunion, logger: logging.Logger):
        self.client_reunion = client_reunion
        self.logger = logger

    def create_reunion(self, data, headers):
        self.logger.info("Creando reunión...")
        return self.client_reunion.create_reunion(data, headers)

    def get_reunion(self, reunion_id: int, headers):
        self.logger.info(f"Obteniendo reunión con ID {reunion_id}")
        return self.client_reunion.get_reunion(reunion_id, headers)

    def list_reuniones(self, page: int, page_size: int, headers, filters: Dict[str, Any]):
        self.logger.info(f"Listando reuniones: page={page}, page_size={page_size}, filtros={filters}")
        return self.client_reunion.list_reuniones(page=page, page_size=page_size, headers=headers, filters=filters)

    def update_reunion(self, reunion_id: int, data, headers):
        self.logger.info(f"Actualizando reunión con ID {reunion_id}")
        return self.client_reunion.update_reunion(reunion_id, data, headers)

    def delete_reunion(self, reunion_id: int, headers):
        self.logger.info(f"Eliminando reunión con ID {reunion_id}")
        return self.client_reunion.delete_reunion(reunion_id, headers)

    def generate_asistencia_code(self, reunion_id: int, headers: Dict[str, Any]):
        self.logger.info(f"Generando código de asistencia para reunión {reunion_id}")
        return self.client_reunion.generate_reunion_code(reunion_id, headers)