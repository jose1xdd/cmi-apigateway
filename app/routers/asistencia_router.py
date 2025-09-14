from fastapi import APIRouter, Depends, Query, Response, status

from app.ioc.container import get_asistencia_manager
from app.models.inputs.asistencia.asistencia_assing import AssingAsistencia
from app.models.inputs.asistencia.asistencia_persona import AsistenciaIndividual
from app.models.inputs.asistencia.user_asistencia_assing import UserAssingAsistencia
from app.models.outputs.paginated_response import PaginatedAsistenciaPersonas
from app.models.outputs.response_estado import EstadoResponse
from app.services.asistencia_manager import AsistenciaManager
from app.utils.constans import BEARER_SCHEME, JSON_HEADER
from app.utils.decorators.role_check_decorator import require_roles


asistencia_router = APIRouter(tags=["Asistencia"], prefix="/asistencia")


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
        reunion_id, data.model_dump(mode="json"), claims)
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
    data: UserAssingAsistencia,
    claims: dict = Depends(require_roles(["usuario"])),
    manager: AsistenciaManager = Depends(get_asistencia_manager),
):
    external_response = manager.user_assign_asistencia(
        reunion_id, data.model_dump(mode="json"), claims)
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
    response_model=PaginatedAsistenciaPersonas,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(BEARER_SCHEME)]
)
def get_personas_with_asistencia(
    reunion_id: int,
    page: int = Query(1, ge=1, description="Número de página"),
    page_size: int = Query(
        10, ge=1, le=100, description="Cantidad de registros por página"),
    claims: dict = Depends(require_roles([])),
    manager: AsistenciaManager = Depends(get_asistencia_manager)
):
    external_response = manager.get_personas_with_asistencia(
        page, page_size, reunion_id, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@asistencia_router.get(
    "/{reunion_id}/persona/{persona_id}",
    response_model=AsistenciaIndividual,
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(BEARER_SCHEME)],
)
def get_personas_with_asistencia(
    reunion_id: int,
    persona_id: int,
    asistencia_manager: AsistenciaManager = Depends(get_asistencia_manager),
    claims: dict = Depends(require_roles(['usuario'])),

):
    external_response = asistencia_manager.get_asistencia_persona(persona_id, reunion_id, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )