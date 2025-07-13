from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.models.inputs.login_input import LoginInput
from app.services.manager import Manager
from app.ioc.container import Container

main_router = APIRouter()


@main_router.post("/login")
@inject
async def login(
    data: LoginInput,
    manager: Manager = Depends(Provide[Container.manager])):
    manager.login(data)
    return {}
