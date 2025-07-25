from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status
from h11 import Response
from pydantic.type_adapter import R

from app.models.inputs.login_input import LoginInput
from app.models.inputs.recovery_password_input import RecoveryPassword
from app.models.inputs.reste_password_input import ResetPassword
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


@main_router.post("/password/recovery", status_code=status.HTTP_202_ACCEPTED)
@inject
async def password_recovery(
        data: RecoveryPassword,
        manager: Manager = Depends(Provide[Container.manager])):

    manager.password_recovery(data)
    return {}

@main_router.post("/password/reset", status_code=status.HTTP_202_ACCEPTED)
@inject
async def password_reset(
        data: ResetPassword,
        manager: Manager = Depends(Provide[Container.manager])):

    manager.password_reset(data)
    return {}