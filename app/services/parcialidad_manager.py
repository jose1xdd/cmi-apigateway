import logging

from app.client.ms_gestion_usuarios.parcialidad.interface.interface_client_parcialidad import IClientParcialidad


class ParcialidadManager:
    def __init__(self,
                 client_parcialidad: IClientParcialidad,
                 logger: logging.Logger):
        self.client_parcialidad = client_parcialidad
        self.logger = logger

    def create_parcialidad(self, data, headers):
        self.logger.info("Creando parcialidad con datos: %s", data)
        return self.client_parcialidad.create_parcialidad(data, headers)

    def update_parcialidad(self, id_parcialidad: str, data, headers):
        self.logger.info(
            "Actualizando parcialidad con id %s y datos: %s", id_parcialidad, data)
        return self.client_parcialidad.update_parcialidad(id_parcialidad, data, headers)

    def delete_parcialidad(self, id_parcialidad: str, headers):
        self.logger.info("Eliminando parcialidad con id %s", id_parcialidad)
        return self.client_parcialidad.delete_parcialidad(id_parcialidad, headers)

    def list_parcialidades(self, page: int, page_size: int, headers, filters):
        self.logger.info(
            "Listando parcialidades con page=%s y page_size=%s", page, page_size)
        return self.client_parcialidad.list_parcialidades(page=page, page_size=page_size, headers=headers, filters=filters)

    def get_parcialidad(self, id_parcialidad: str, headers):
        self.logger.info("Consultando parcialidad con id %s", id_parcialidad)
        return self.client_parcialidad.get_parcialidad(id_parcialidad, headers)
