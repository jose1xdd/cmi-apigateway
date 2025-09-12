import logging
from typing import Any, Dict

from app.client.ms_gestion_reuniones.asistencia.interface.interface_client_asistencia import IClientAsistencia


class AsistenciaManager:
    def __init__(self, client_asistencia: IClientAsistencia, logger: logging.Logger):
        self.client_asistencia = client_asistencia
        self.logger = logger

    def assign_asistencia(self, reunion_id: int, data: Dict[str, Any], headers):
        self.logger.info(f"Asginando asistencia en la reunión {reunion_id}")
        return self.client_asistencia.assign_asistencia(reunion_id, data, headers)

    def user_assign_asistencia(self, reunion_id: int, data: Dict[str, Any], headers):
        self.logger.info(
            f"Asginando asistencia de usuario en la reunión {reunion_id}")
        return self.client_asistencia.user_assign_asistencia(reunion_id, data, headers)

    def delete_asistencia(self, reunion_id: int, persona_id: int, headers):
        self.logger.info(
            f"Eliminando asistencia para persona_id={persona_id} en reunion_id={reunion_id}"
        )
        return self.client_asistencia.delete_asistencia(reunion_id, persona_id, headers)
