# app/routers/reportes_router.py

from fastapi import APIRouter, Depends, Response
from fastapi.responses import StreamingResponse
from io import BytesIO

from app.ioc.container import get_reportes_manager
from app.services.reporte_manager import ReporteManager
from app.utils.constans import BEARER_SCHEME
from app.utils.decorators.role_check_decorator import require_roles

reportes_router = APIRouter(tags=["Reportes"])

# Puedes inyectar la URL del microservicio desde env


@reportes_router.get(
    "/reportes/personas",
    responses={200: {"content": {
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": {}}}},
    summary="Descargar reporte de personas", dependencies=[Depends(BEARER_SCHEME)]
)
def descargar_reporte_personas(
    claims: dict = Depends(require_roles([])),
    manager: ReporteManager = Depends(get_reportes_manager)
):
    response = manager.get_reporte_personas(claims)

    # Si es éxito (archivo Excel)
    if response.status_code == 200 and \
       response.headers.get("content-type") == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        return StreamingResponse(
            response.raw,
            media_type=response.headers.get("content-type"),
            headers={"Content-Disposition": "attachment; filename=personas.xlsx"},
            status_code=response.status_code,
        )

    # Si vino error en JSON u otro tipo de respuesta
    return Response(
        content=response.content,
        media_type=response.headers.get("content-type", "application/json"),
        status_code=response.status_code,
    )


@reportes_router.get(
    "/reporte/asistencia/{reunion_id}",
    responses={200: {"content": {
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": {}}}},
    summary="Descargar reporte de asistencia de un reunion", dependencies=[Depends(BEARER_SCHEME)]
)
def descargar_reporte_personas(
    reunion_id: int,
    claims: dict = Depends(require_roles([])),
    manager: ReporteManager = Depends(get_reportes_manager)
):
    response = manager.get_reporte_asistencia(reunion_id, claims)

    # Si es éxito (archivo Excel)
    if response.status_code == 200 and \
       response.headers.get("content-type") == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        return StreamingResponse(
            response.raw,
            media_type=response.headers.get("content-type"),
            headers={
                "Content-Disposition": f"attachment; filename=reporte_asistencia_reunion{reunion_id}.xlsx"},
            status_code=response.status_code,
        )

    # Si vino error en JSON u otro tipo de respuesta
    return Response(
        content=response.content,
        media_type=response.headers.get("content-type", "application/json"),
        status_code=response.status_code,
    )
