from typing import Optional
from fastapi import APIRouter, Depends, Query, Response, status

from app.ioc.container import get_asistencia_manager
from app.models.inputs.asistencia.asistencia_assing import AssingAsistencia
from app.models.inputs.asistencia.user_asistencia_assing import UserRegisterAsistencia
from app.models.outputs.paginated_response import PaginatedAsistenciaPersonas
from app.models.outputs.response_estado import EstadoResponse
from app.utils.constans import BEARER_SCHEME, JSON_HEADER
from app.utils.decorators.role_check_decorator import require_roles
from app.services.asistencia_manager import AsistenciaManager


asistencia_router = APIRouter(prefix="/asistencia", tags=["Asistencia"])


@asistencia_router.post(
    "/assign/{reunion_id}",
    status_code=status.HTTP_201_CREATED,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def assign_asistencia(
    reunion_id: int,
    data: AssingAsistencia,
    claims: dict = Depends(require_roles([])),
    manager: AsistenciaManager = Depends(get_asistencia_manager),
):
    external_response = manager.assign_asistencia(
        reunion_id, data.model_dump(mode="json"), claims
    )
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@asistencia_router.post(
    "/user-assign/{reunion_id}",
    status_code=status.HTTP_201_CREATED,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def user_assign_asistencia(
    reunion_id: int,
    data: UserRegisterAsistencia,
    claims: dict = Depends(require_roles([])),
    manager: AsistenciaManager = Depends(get_asistencia_manager),
):
    external_response = manager.user_assign_asistencia(
        reunion_id, data.model_dump(mode="json"), claims
    )
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@asistencia_router.delete(
    "/{reunion_id}/{persona_id}",
    status_code=status.HTTP_200_OK,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def delete_asistencia(
    reunion_id: int,
    persona_id: int,
    claims: dict = Depends(require_roles([])),
    manager: AsistenciaManager = Depends(get_asistencia_manager),
):
    external_response = manager.delete_asistencia(
        reunion_id, persona_id, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@asistencia_router.get(
    "/{reunion_id}/personas",
    status_code=status.HTTP_200_OK,
    response_model=PaginatedAsistenciaPersonas,
    dependencies=[Depends(BEARER_SCHEME)],
)
def get_personas_with_asistencia(
    reunion_id: int,
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    numero_documento: Optional[str] = Query(None),
    nombre: Optional[str] = Query(None),
    apellido: Optional[str] = Query(None),
    claims: dict = Depends(require_roles([])),
    manager: AsistenciaManager = Depends(get_asistencia_manager),
):
    external_response = manager.get_personas_with_asistencia(
        page=page,
        page_size=page_size,
        reunion_id=reunion_id,
        headers=claims,
        numero_documento=numero_documento,
        nombre=nombre,
        apellido=apellido,
    )
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@asistencia_router.get(
    "/{reunion_id}/persona/{persona_id}",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(BEARER_SCHEME)],
)
def get_asistencia_persona(
    reunion_id: int,
    persona_id: int,
    claims: dict = Depends(require_roles([])),
    manager: AsistenciaManager = Depends(get_asistencia_manager),
):
    external_response = manager.get_asistencia_persona(
        persona_id, reunion_id, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )
