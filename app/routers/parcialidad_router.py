from typing import Optional
from fastapi import APIRouter, Depends, File, Query, Response, UploadFile, status

from app.ioc.container import get_parcialidad_manager
from app.models.inputs.parcialidad.parcialidad_create import ParcialidadCreate
from app.models.inputs.parcialidad.parcialidad_filter import ParcialidadFilter
from app.models.outputs.paginated_response import PaginatedParcialidad
from app.models.outputs.parcialidad.parcialidad_output import ParcialidadOut
from app.models.outputs.response_estado import EstadoResponse
from app.services.parcialidad_manager import ParcialidadManager
from app.utils.constans import BEARER_SCHEME, JSON_HEADER
from app.utils.decorators.role_check_decorator import require_roles


parcialidad_router = APIRouter(tags=["Parcialidad"])


@parcialidad_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def create_parcialidad(
    data: ParcialidadCreate,
    claims: dict = Depends(require_roles([])),
    manager: ParcialidadManager = Depends(get_parcialidad_manager),
):
    external_response = manager.create_parcialidad(
        data.model_dump(mode='json'), claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@parcialidad_router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def delete_parcialidad(
    id: str,
    claims: dict = Depends(require_roles([])),
    manager: ParcialidadManager = Depends(get_parcialidad_manager),
):
    external_response = manager.delete_parcialidad(id, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@parcialidad_router.get("/", status_code=status.HTTP_200_OK, response_model=PaginatedParcialidad, dependencies=[Depends(BEARER_SCHEME)])
async def list_parcialidades(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    claims: dict = Depends(require_roles(["usuario"])),
    filters: ParcialidadFilter = Depends(),
    manager: ParcialidadManager = Depends(get_parcialidad_manager),
):
    external_response = manager.list_parcialidades(
        page, page_size, claims, filters.model_dump(exclude_none=True))
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@parcialidad_router.get("/{id_parcialidad}", status_code=status.HTTP_200_OK, response_model=ParcialidadOut, dependencies=[Depends(BEARER_SCHEME)])
async def get_parcialidad(
    id_parcialidad: str,
    claims: dict = Depends(require_roles(["usuario"])),
    manager: ParcialidadManager = Depends(get_parcialidad_manager),
):
    external_response = manager.get_parcialidad(id_parcialidad, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@parcialidad_router.put("/{id}", status_code=status.HTTP_200_OK, response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def update_parcialidad(
    id: str,
    data: ParcialidadCreate,
    claims: dict = Depends(require_roles([])),
    manager: ParcialidadManager = Depends(get_parcialidad_manager),
):
    external_response = manager.update_parcialidad(
        id, data.model_dump(mode='json'), claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@parcialidad_router.post("/upload-excel", dependencies=[Depends(BEARER_SCHEME)])
async def upload_excel(
    file: UploadFile = File(...),
    claims: dict = Depends(require_roles([])),
    manager: ParcialidadManager = Depends(get_parcialidad_manager),

):
    """
    Endpoint del API Gateway para cargar parcialidades vía Excel.
    """

    response = await manager.upload_excel(file, headers=claims)
    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get("Content-Type", JSON_HEADER),
    )
