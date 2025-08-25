
from fastapi import APIRouter, Depends, Query, Response, status

from app.ioc.container import get_familia_manager
from app.models.inputs.familia.familia_create import FamiliaCreate
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
