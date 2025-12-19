import requests
from typing import Dict, Any, Optional
from app.client.ms_gestion_usuarios.familia.interface.interface_client_familia import IClientFamilia
from app.utils.constans import JSON_HEADER


class ClientFamilia(IClientFamilia):
    def __init__(self, url: str):
        self.url = url.rstrip("/")

    # 🔹 Crear familia
    def create_familia(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.post(f"{self.url}/familias/create", json=body, headers=merged_headers)

    # 🔹 Eliminar familia
    def delete_familia(self, id_familia: int, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.delete(f"{self.url}/familias/{id_familia}", headers=merged_headers)

    # 🔹 Listar familias
    def list_familias(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        params = {"page": page, "page_size": page_size}
        return requests.get(f"{self.url}/familias", params=params, headers=merged_headers)

    # 🔹 Buscar familias (por nombre/apellido/cédula del líder)
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
        merged_headers = {**JSON_HEADER, **(headers or {})}

        params = {
            "query": query,
            "page": page,
            "page_size": page_size,
        }

        if parcialidad_id is not None:
            params["parcialidad_id"] = parcialidad_id

        if rango_miembros:
            params["rango_miembros"] = rango_miembros

        if estado:
            params["estado"] = estado

        return requests.get(
            f"{self.url}/familias/search",
            params=params,
            headers=merged_headers
        )

    # 🔹 Obtener datos con líder/parcialidad

    def get_familias_leaderdata(self, page: int = 1, page_size: int = 10, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        params = {"page": page, "page_size": page_size}
        return requests.get(f"{self.url}/familias/get/leader-data", params=params, headers=merged_headers)

    # 🔹 Obtener miembros de familia
    def get_miembros_familia(self, id_familia: int, page: int = 1, page_size: int = 10, query: Optional[str] = None, headers: Optional[Dict[str, str]] = None, vivos: Optional[bool] = False):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        params = {"page": page, "page_size": page_size}
        if query:
            params["query"] = query
        if vivos:
            params["vivos"] = vivos
        return requests.get(f"{self.url}/familias/{id_familia}/miembros", params=params, headers=merged_headers)

    # 🔹 Obtener resumen de familia
    def get_familia_resumen(self, id_familia: int, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(f"{self.url}/familias/{id_familia}/resumen", headers=merged_headers)

    # 🔹 Obtener estadísticas generales
    def get_estadisticas_generales(self, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(f"{self.url}/familias/estadisticas-generales", headers=merged_headers)

    # 🔹 Obtener familia por ID
    def get_familia(self, id_familia: int, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(f"{self.url}/familias/{id_familia}", headers=merged_headers)

    # 🔹 Carga masiva desde Excel
    def upload_excel(self, filename: str, file_bytes: bytes, headers: Optional[Dict[str, str]] = None):
        merged_headers = {**(headers or {})}
        files = {"file": (
            filename, file_bytes, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")}
        return requests.post(f"{self.url}/familias/upload-excel", files=files, headers=merged_headers)

    def update_familia(self, body: Dict[str, Any], headers: Optional[Dict[str, str]] = None):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.put(f"{self.url}/familias/update", json=body, headers=merged_headers)
