from typing import List, Optional, Dict, Any
from fastapi import APIRouter, Depends, Form, File, UploadFile, Query, Response, status

from app.ioc.container import get_index_manager
from app.models.inputs.publicacion.publicacion_filters import PublicacionFilter
from app.models.outputs.paginated_response import PaginatedPublicacion
from app.models.outputs.publicacion.publicacion_update import PublicacionUpdate
from app.models.outputs.response_estado import EstadoResponse
from app.utils.constans import JSON_HEADER, BEARER_SCHEME
from app.utils.decorators.role_check_decorator import require_roles
from app.services.index_manager import IndexManager


index_router = APIRouter(prefix="/index", tags=["Index"])


@index_router.post(
    "/create",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def create_publicacion(
    titulo: str = Form(...),
    contenido: Optional[str] = Form(None),
    fotos: Optional[List[UploadFile]] = File(None),
    claims: dict = Depends(require_roles([])),
    manager: IndexManager = Depends(get_index_manager),
):
    fotos_bytes = [await f.read() for f in fotos] if fotos else None
    body: Dict[str, Any] = {"titulo": titulo, "contenido": contenido}

    external_response = manager.create_publicacion(
        body, fotos=fotos_bytes, headers=claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@index_router.post(
    "/{publicacion_id}/fotos",
    status_code=status.HTTP_201_CREATED,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def agregar_fotos(
    publicacion_id: int,
    fotos: List[UploadFile] = File(...),
    claims: dict = Depends(require_roles([])),
    manager: IndexManager = Depends(get_index_manager),
):
    fotos_bytes = [await f.read() for f in fotos]

    external_response = manager.agregar_fotos(
        publicacion_id, fotos_bytes, headers=claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@index_router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=PaginatedPublicacion,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def get_all_publicacion(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=100),
    filters: PublicacionFilter = Depends(),
    manager: IndexManager = Depends(get_index_manager),
):
    external_response = manager.get_all_publicacion(
        page, page_size, filters=filters.model_dump(exclude_none=True))
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@index_router.get(
    "/{foto_id}",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "content": {"image/png": {}},
            "description": "Imagen en binario",
        },
        404: {"description": "Foto no encontrada"},
    },
    dependencies=[Depends(BEARER_SCHEME)],
)
async def get_foto_by_id(
    foto_id: int,
    manager: IndexManager = Depends(get_index_manager),
):
    external_response = manager.get_foto_by_id(foto_id)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", "image/png"),
    )


@index_router.put(
    "/{publicacion_id}",
    status_code=status.HTTP_200_OK,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def update_publicacion(
    publicacion_id: int,
    body: PublicacionUpdate,
    claims: dict = Depends(require_roles([])),
    manager: IndexManager = Depends(get_index_manager),
):
    external_response = manager.update_publicacion(
        publicacion_id, body.model_dump(), headers=claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@index_router.delete(
    "/foto/{foto_id}",
    status_code=status.HTTP_200_OK,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def eliminar_foto(
    foto_id: int,
    claims: dict = Depends(require_roles([])),
    manager: IndexManager = Depends(get_index_manager),
):
    external_response = manager.eliminar_foto(foto_id, headers=claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@index_router.delete(
    "/{publicacion_id}",
    status_code=status.HTTP_200_OK,
    response_model=EstadoResponse,
    dependencies=[Depends(BEARER_SCHEME)],
)
async def eliminar_publicacion(
    publicacion_id: int,
    claims: dict = Depends(require_roles([])),
    manager: IndexManager = Depends(get_index_manager),
):
    external_response = manager.eliminar_publicacion(
        publicacion_id, headers=claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )
