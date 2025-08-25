from fastapi import APIRouter, Depends, Query, Response, status

from app.ioc.container import get_persona_manager
from app.models.inputs.familia.assing_familia_users import AssingFamilia
from app.models.inputs.persona.persona_create import PersonaCreate
from app.models.inputs.persona.persona_filter import PersonaFilter
from app.models.inputs.persona.persona_update import PersonaUpdate
from app.models.outputs.familia.familia_asignacion_response import AsignacionFamiliaResponse
from app.models.outputs.paginated_response import PaginatedPersonas
from app.models.outputs.persona.persona_output import PersonaOut
from app.models.outputs.response_estado import EstadoResponse
from app.services.persona_manager import PersonaManager
from app.utils.constans import BEARER_SCHEME, JSON_HEADER
from app.utils.decorators.role_check_decorator import require_roles


persona_router = APIRouter(tags=["Persona"])


@persona_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def create_persona(
    data: PersonaCreate,
    claims: dict = Depends(require_roles([])),
    manager: PersonaManager = Depends(get_persona_manager),
):
    external_response = manager.create_person(data.model_dump(mode='json'), claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@persona_router.put("/{id}", status_code=status.HTTP_200_OK, response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def update_persona(
    id: str,
    data: PersonaUpdate,
    claims: dict = Depends(require_roles(["usuario"])),
    manager: PersonaManager = Depends(get_persona_manager),
):
    external_response = manager.update_person(id, data.model_dump(mode='json'), claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@persona_router.delete("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def delete_persona(
    id: str,
    claims: dict = Depends(require_roles([])),
    manager: PersonaManager = Depends(get_persona_manager),
):
    external_response = manager.delete_person(id, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@persona_router.get("/", status_code=status.HTTP_200_OK, response_model=PaginatedPersonas, dependencies=[Depends(BEARER_SCHEME)])
async def list_personas(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    claims: dict = Depends(require_roles(["usuario"])),
    filters: PersonaFilter = Depends(),
    manager: PersonaManager = Depends(get_persona_manager),
):
    external_response = manager.list_personas(page, page_size, claims,filters.model_dump(exclude_none=True))
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@persona_router.get("/{id_persona}", status_code=status.HTTP_200_OK, response_model=PersonaOut, dependencies=[Depends(BEARER_SCHEME)])
async def get_persona(
    id_persona: str,
    claims: dict = Depends(require_roles(["usuario"])),
    manager: PersonaManager = Depends(get_persona_manager),
):
    external_response = manager.get_persona(id_persona, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@persona_router.patch("/assing-family", response_model=AsignacionFamiliaResponse, dependencies=[Depends(BEARER_SCHEME)])
def assing_family_users(
    data: AssingFamilia,
    claims: dict = Depends(require_roles([])),
    manager: PersonaManager = Depends(get_persona_manager)
):
    external_response = manager.assing_familia(data.model_dump(mode='json'), claims)

    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get(
            "Content-Type", JSON_HEADER),
    )
