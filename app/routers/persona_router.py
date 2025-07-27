from fastapi import APIRouter, Depends, Query, Request, Response, status

from app.ioc.container import get_persona_manager
from app.services.persona_manager import PersonaManager
from app.utils.constans import JSON_HEADER
from app.utils.decorators.role_check_decorator import require_roles


persona_router = APIRouter()


@persona_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_persona(
    data: Request,
    claims: dict = Depends(require_roles(["admin"])),
    manager: PersonaManager = Depends(get_persona_manager),
):
    body = await data.json()
    external_response = manager.create_person(body, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@persona_router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_persona(
    id: str,
    data: Request,
    claims: dict = Depends(require_roles(["admin"])),
    manager: PersonaManager = Depends(get_persona_manager),
):
    body = await data.json()
    external_response = manager.update_person(id, body, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@persona_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_persona(
    id: str,
    claims: dict = Depends(require_roles(["admin"])),
    manager: PersonaManager = Depends(get_persona_manager),
):
    external_response = manager.delete_person(id, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@persona_router.get("/", status_code=status.HTTP_200_OK)
async def list_personas(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    claims: dict = Depends(require_roles(["admin"])),
    manager: PersonaManager = Depends(get_persona_manager),
):
    external_response = manager.list_personas(page, page_size, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )
