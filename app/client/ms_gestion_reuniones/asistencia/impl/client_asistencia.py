import requests
from typing import Dict, Any, Optional

from app.client.ms_gestion_reuniones.asistencia.interface.interface_client_asistencia import IClientAsistencia
from app.utils.constans import JSON_HEADER


class ClientAsistencia(IClientAsistencia):
    def __init__(self, url: str):
        self.url = url.rstrip("/")

    def assign_asistencia(
        self,
        reunion_id: int,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ):
        """
        Asigna asistencia a varias personas en una reunión
        """
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.post(
            f"{self.url}/asistencia/assign/{reunion_id}",
            json=body,
            headers=merged_headers
        )

    def user_assign_asistencia(
        self,
        reunion_id: int,
        body: Dict[str, Any],
        headers: Optional[Dict[str, str]] = None
    ):
        """
        Asigna asistencia para un usuario específico en una reunión
        """
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.post(
            f"{self.url}/asistencia/user-assign/{reunion_id}",
            json=body,
            headers=merged_headers
        )

    def delete_asistencia(
        self,
        reunion_id: int,
        persona_id: int,
        headers: Optional[Dict[str, str]] = None
    ):
        """
        Elimina asistencia por reunion_id y persona_id
        """
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.delete(
            f"{self.url}/asistencia/{reunion_id}/{persona_id}",
            headers=merged_headers
        )

    def get_personas_with_asistencia(
        self,
        reunion_id: int,
        page: int,
        page_size: int,
        headers: Optional[Dict[str, str]] = None,
        query: Optional[str] = None,
    ):
        """
        Obtiene listado paginado de personas con cruce de asistencia
        """
        merged_headers = {**JSON_HEADER, **(headers or {})}

        params = {
            "page": page,
            "page_size": page_size,
        }

        if query:
            params["query"] = query

        return requests.get(
            f"{self.url}/asistencia/{reunion_id}/personas",
            params=params,
            headers=merged_headers
        )

    def get_asistencia_persona(self, persona_id: int, reunion_id: int, headers):
        merged_headers = {**JSON_HEADER, **(headers or {})}
        return requests.get(
            f"{self.url}/asistencia/{reunion_id}/persona/{persona_id}",
            headers=merged_headers
        )
