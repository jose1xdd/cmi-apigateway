import logging
from typing import Any, Dict, Optional
from app.client.ms_gestion_reuniones.asistencia.interface.interface_client_asistencia import IClientAsistencia


class AsistenciaManager:
    def __init__(self, client_asistencia: IClientAsistencia, logger: logging.Logger):
        self.client_asistencia = client_asistencia
        self.logger = logger

    def assign_asistencia(self, reunion_id: int, data: Dict[str, Any], headers):
        self.logger.info(f"[AsistenciaManager] Asignando asistencia en reunión {reunion_id}")
        return self.client_asistencia.assign_asistencia(reunion_id, data, headers)

    def user_assign_asistencia(self, reunion_id: int, data: Dict[str, Any], headers):
        self.logger.info(f"[AsistenciaManager] Registrando asistencia (por documento) en reunión {reunion_id}")
        return self.client_asistencia.user_assign_asistencia(reunion_id, data, headers)

    def delete_asistencia(self, reunion_id: int, persona_id: int, headers):
        self.logger.info(f"[AsistenciaManager] Eliminando asistencia persona_id={persona_id}, reunión={reunion_id}")
        return self.client_asistencia.delete_asistencia(reunion_id, persona_id, headers)

    def get_personas_with_asistencia(
        self,
        page: int,
        page_size: int,
        reunion_id: int,
        headers,
        numero_documento: Optional[str] = None,
        nombre: Optional[str] = None,
        apellido: Optional[str] = None,
    ):
        return self.client_asistencia.get_personas_with_asistencia(
            reunion_id=reunion_id,
            page=page,
            page_size=page_size,
            headers=headers,
            numero_documento=numero_documento,
            nombre=nombre,
            apellido=apellido,
        )

    def get_asistencia_persona(self, persona_id: int, reunion_id: int, headers):
        return self.client_asistencia.get_asistencia_persona(persona_id, reunion_id, headers)
