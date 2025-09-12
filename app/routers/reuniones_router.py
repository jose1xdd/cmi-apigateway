from fastapi import APIRouter, Depends, Query, Response, status

from app.ioc.container import get_reunion_manager
from app.models.inputs.reunion.reunion_create import ReunionCreate
from app.models.inputs.reunion.reunion_filters import ReunionFilter
from app.models.inputs.reunion.reunion_update import ReunionUpdate
from app.models.outputs.response_estado import EstadoResponse
from app.models.outputs.reunion.reunion_out import ReunionOut
from app.models.outputs.paginated_response import PaginatedReunion
from app.services.reunion_manager import ReunionManager
from app.utils.constans import BEARER_SCHEME, JSON_HEADER
from app.utils.decorators.role_check_decorator import require_roles


reunion_router = APIRouter(tags=["Reunion"], prefix="/reunion")


@reunion_router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def create_reunion(
    data: ReunionCreate,
    claims: dict = Depends(require_roles([])),
    manager: ReunionManager = Depends(get_reunion_manager),
):
    external_response = manager.create_reunion(data.model_dump(mode="json"), claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@reunion_router.get(
    "/{reunion_id}",
    status_code=status.HTTP_200_OK,
    response_model=ReunionOut,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def get_reunion(
    reunion_id: int,
    claims: dict = Depends(require_roles(["usuario"])),
    manager: ReunionManager = Depends(get_reunion_manager),
):
    external_response = manager.get_reunion(reunion_id, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@reunion_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=PaginatedReunion,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def list_reuniones(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    filters: ReunionFilter = Depends(),
    claims: dict = Depends(require_roles(["usuario"])),
    manager: ReunionManager = Depends(get_reunion_manager),
):
    external_response = manager.list_reuniones(page, page_size, claims, filters.model_dump(exclude_none=True))
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@reunion_router.put(
    "/{reunion_id}",
    status_code=status.HTTP_200_OK,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def update_reunion(
    reunion_id: int,
    data: ReunionUpdate,
    claims: dict = Depends(require_roles(["usuario"])),
    manager: ReunionManager = Depends(get_reunion_manager),
):
    external_response = manager.update_reunion(reunion_id, data.model_dump(mode="json"), claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@reunion_router.delete(
    "/{reunion_id}",
    status_code=status.HTTP_200_OK,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def delete_reunion(
    reunion_id: int,
    claims: dict = Depends(require_roles([])),
    manager: ReunionManager = Depends(get_reunion_manager),
):
    external_response = manager.delete_reunion(reunion_id, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )

@reunion_router.patch(
    "/{reunion_id}/generate-asistencia-code",
    status_code=status.HTTP_200_OK,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def generate_asistencia_code(
    reunion_id: int,
    claims: dict = Depends(require_roles([])),
    manager: ReunionManager = Depends(get_reunion_manager),
):
    external_response = manager.generate_asistencia_code(reunion_id, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )