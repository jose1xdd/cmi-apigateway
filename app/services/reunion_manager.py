import logging
from typing import Any, Dict
from app.client.ms_gestion_reuniones.reunion.interface.interface_gestion_reuniones import IClientReunion


class ReunionManager:
    def __init__(self, client_reunion: IClientReunion, logger: logging.Logger):
        self.client_reunion = client_reunion
        self.logger = logger

    def create_reunion(self, data, headers):
        self.logger.info("[ReunionManager] Creando reunión...")
        return self.client_reunion.create_reunion(data, headers)

    def get_reunion(self, reunion_id: int, headers):
        self.logger.info(f"[ReunionManager] Obteniendo reunión ID={reunion_id}")
        return self.client_reunion.get_reunion(reunion_id, headers)

    def list_reuniones(self, page: int, page_size: int, headers, filters: Dict[str, Any]):
        self.logger.info(f"[ReunionManager] Listando reuniones con filtros={filters}")
        return self.client_reunion.list_reuniones(page=page, page_size=page_size, headers=headers, filters=filters)

    def update_reunion(self, reunion_id: int, data, headers):
        self.logger.info(f"[ReunionManager] Actualizando reunión ID={reunion_id}")
        return self.client_reunion.update_reunion(reunion_id, data, headers)

    def delete_reunion(self, reunion_id: int, headers):
        self.logger.info(f"[ReunionManager] Eliminando reunión ID={reunion_id}")
        return self.client_reunion.delete_reunion(reunion_id, headers)

    def abrir_reunion(self, reunion_id: int, headers: Dict[str, Any]):
        self.logger.info(f"[ReunionManager] Abriendo reunión ID={reunion_id}")
        return self.client_reunion.abrir_reunion(reunion_id, headers)

    def cerrar_reunion(self, reunion_id: int, headers: Dict[str, Any]):
        self.logger.info(f"[ReunionManager] Cerrando reunión ID={reunion_id}")
        return self.client_reunion.cerrar_reunion(reunion_id, headers)
