
from typing import Optional
from fastapi import APIRouter, Depends, File, Query, Response, UploadFile, status

from app.ioc.container import get_familia_manager
from app.models.inputs.familia.familia_create import EnumEstadoFamilia, FamiliaCreate
from app.models.inputs.persona.persona_carga_masiva import CargaMasivaResponse
from app.models.outputs.paginated_response import PaginatedFamilias
from app.models.outputs.persona.persona_output import PersonaOut
from app.models.outputs.response_estado import EstadoResponse
from app.services.familia_manager import FamiliaManager
from app.utils.constans import BEARER_SCHEME, JSON_HEADER
from app.utils.decorators.role_check_decorator import require_roles


familia_router = APIRouter(tags=["Familia"])


@familia_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def create_familia(data: FamiliaCreate,
                         claims: dict = Depends(require_roles([])),
                         manager: FamiliaManager = Depends(get_familia_manager)):
    external_response = manager.create_familia(data.model_dump(mode='json'), claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@familia_router.delete("/{id_familia}", status_code=status.HTTP_200_OK, response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def delete_familia(id_familia: int,
                         claims: dict = Depends(require_roles([])),
                         manager: FamiliaManager = Depends(get_familia_manager)):
    external_response = manager.delete_familia(id_familia, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@familia_router.get("/", status_code=status.HTTP_200_OK, response_model=PaginatedFamilias, dependencies=[Depends(BEARER_SCHEME)])
async def list_familias(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1),
    claims: dict = Depends(require_roles(["usuario"])),
    manager: FamiliaManager = Depends(get_familia_manager),
):
    external_response = manager.list_familias(page, page_size, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )



@familia_router.post("/upload-excel", status_code=status.HTTP_201_CREATED, response_model=CargaMasivaResponse, dependencies=[Depends(BEARER_SCHEME)])
async def upload_excel(
    file: UploadFile = File(...),
    claims: dict = Depends(require_roles([])),
    manager: FamiliaManager = Depends(get_familia_manager)
):
    response = await manager.upload_excel(file, claims)
    return Response(
        content=response.content,
        status_code=response.status_code,
        media_type=response.headers.get("Content-Type", JSON_HEADER),
    )

@familia_router.get(
    "/search",
    dependencies=[Depends(BEARER_SCHEME)],
    response_model=PaginatedFamilias
)
def search_familias(
    query: Optional[str] = Query(None),
    parcialidad_id: Optional[int] = Query(None),
    rango_miembros: Optional[str] = Query(None, pattern="^(1-3|4-6|7\+)$"),
    estado: Optional[EnumEstadoFamilia] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=100),
    claims: dict = Depends(require_roles(["usuario"])),
    manager: FamiliaManager = Depends(get_familia_manager)
):
    external_response = manager.search_familias(
        query=query,
        parcialidad_id=parcialidad_id,
        rango_miembros=rango_miembros,
        estado=estado,
        page=page,
        page_size=page_size,
        headers=claims
    )

    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )



@familia_router.get("/get/leader-data", dependencies=[Depends(BEARER_SCHEME)])
def get_familias_leaderdata(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=100),
    claims: dict = Depends(require_roles(["usuario"])),
    manager: FamiliaManager = Depends(get_familia_manager)
):
    external_response = manager.get_familias_leaderdata(page, page_size, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )



@familia_router.get("/estadisticas-generales", dependencies=[Depends(BEARER_SCHEME)])
def get_estadisticas_generales(
    claims: dict = Depends(require_roles(["usuario"])),
    manager: FamiliaManager = Depends(get_familia_manager)
):
    external_response = manager.get_estadisticas_generales(claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )

@familia_router.get("/{id_familia}/resumen", dependencies=[Depends(BEARER_SCHEME)])
def get_familia_resumen(
    id_familia: int,
    claims: dict = Depends(require_roles(["usuario"])),
    manager: FamiliaManager = Depends(get_familia_manager)
):
    external_response = manager.get_familia_resumen(id_familia, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )

@familia_router.get("/{id_familia}/miembros", dependencies=[Depends(BEARER_SCHEME)])
def get_miembros_familia(
    id_familia: int,
    query: str | None = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=100),
    claims: dict = Depends(require_roles(["usuario"])),
    manager: FamiliaManager = Depends(get_familia_manager)
):
    external_response = manager.get_miembros_familia(id_familia, page, page_size, query, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )

@familia_router.get("/{id_familia}", status_code=status.HTTP_200_OK, response_model=PersonaOut, dependencies=[Depends(BEARER_SCHEME)])
async def get_familia(
    id_familia: int,
    claims: dict = Depends(require_roles(["usuario"])),
    manager: FamiliaManager = Depends(get_familia_manager),
):
    external_response = manager.get_familia(id_familia, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )