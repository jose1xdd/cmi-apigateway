import logging

from app.client.ms_reportes.reportes.interface.interface_client_reportes import IClientReportes


class ReporteManager:
    def __init__(self, client_reportes: IClientReportes, logger: logging.Logger):
        self.logger = logger
        self.client_reportes = client_reportes

    def get_reporte_personas(self, headers):
        self.logger.info(
            "Solicitando reporte de personas al microservicio de reportes")
        return self.client_reportes.get_reporte_personas(headers)

    def get_reporte_asistencia(self, reunion_id: int, headers):
        self.logger.info(
            "Solicitando reporte de asistencia al microservicio de reportes")
        return self.client_reportes.get_reporte_asistencia(reunion_id, headers)
    
    def get_reporte_familia(self, familia_id: int, headers):
        self.logger.info("Solicitando reporte de familia al microservicio de reportes")
        return self.client_reportes.get_reporte_familia(familia_id, headers)
    
    def get_resumen_dashboard(self, headers):
        self.logger.info("Solicitando resumen general del dashboard al microservicio de reportes")
        return self.client_reportes.get_resumen_dashboard(headers)
