import logging
from fastapi.responses import StreamingResponse

from app.client.ms_reportes.censo.interface.inteface_client_censo import IClientCenso


class CensoManager:
    def __init__(self, client_censo: IClientCenso, logger: logging.Logger):
        self.client_censo:IClientCenso = client_censo
        self.logger = logger

    def generar_censo(self, payload: dict):
        self.logger.info(
            "Solicitando generación de censo al microservicio de censo")
        response = self.client_censo.generar_censo(payload)
        return response.json(), response.status_code

    def listar_procesos(self, params: dict):
        self.logger.info("Solicitando listado de procesos de censo")
        response = self.client_censo.listar_procesos(params)
        return response.json(), response.status_code

    def exportar_censo(self, censo_proceso_id: int):
        self.logger.info(
            f"Solicitando exportación de censo {censo_proceso_id}")
        response = self.client_censo.exportar_censo(censo_proceso_id)
        return StreamingResponse(
            response.raw,
            media_type=response.headers.get("content-type"),
            headers={
                "Content-Disposition": f"attachment; filename=censo_proceso_{censo_proceso_id}.xlsx"
            },
            status_code=response.status_code,
        )
