from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.services.manager import Manager
from app.ioc.container import Container

main_router = APIRouter()


@main_router.get("/login")
@inject
async def login(
    manager: Manager = Depends(Provide[Container.manager])
):
    return {"message": "Usuario creado", "user": manager.test()}
