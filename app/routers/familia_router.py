
from typing import Any, Dict
from fastapi import APIRouter, Depends, Query, Request, Response, status

from app.ioc.container import get_familia_manager
from app.services.familia_manager import FamiliaManager
from app.utils.constans import JSON_HEADER
from app.utils.decorators.role_check_decorator import require_roles


familia_router = APIRouter(tags=["Familia"])


@familia_router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_familia(data: Request,
                         claims: dict = Depends(require_roles(["admin"])),
                         manager: FamiliaManager = Depends(get_familia_manager)):
    body = await data.json()
    external_response = manager.create_familia(body, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@familia_router.delete("/{id_familia}", status_code=status.HTTP_200_OK)
async def delete_familia(id_familia: int,
                         claims: dict = Depends(require_roles(["admin"])),
                         manager: FamiliaManager = Depends(get_familia_manager)):
    external_response = manager.delete_familia(id_familia, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )


@familia_router.get("/", status_code=status.HTTP_200_OK)
async def list_familias(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1),
    claims: dict = Depends(require_roles(["admin"])),
    manager: FamiliaManager = Depends(get_familia_manager),
):
    external_response = manager.list_familias(page, page_size, claims)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", JSON_HEADER),
    )
