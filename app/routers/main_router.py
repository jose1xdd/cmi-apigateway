from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.models.inputs.login_input import LoginInput
from app.services.manager import Manager
from app.ioc.container import Container
from app.utils.decorators.role_check_decorator import require_roles

main_router = APIRouter()


@main_router.post("/login")
@inject
async def login(
        data: LoginInput,
        manager: Manager = Depends(Provide[Container.manager])):

    return manager.login(data)
@main_router.post("/test")
@inject
async def login(
        manager: Manager = Depends(Provide[Container.manager])):

    manager.test()
    return {}
@main_router.post("/test2")
@inject
async def login(
        data: LoginInput,
        claims: dict = Depends(require_roles(["admin"])),
        manager: Manager = Depends(Provide[Container.manager])):

    manager.login(data)
    return {}