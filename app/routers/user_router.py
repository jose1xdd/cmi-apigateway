from dependency_injector.wiring import inject
from fastapi import APIRouter, Depends, status

from app.ioc.container import get_user_manager
from app.models.inputs.login_input import LoginInput
from app.models.inputs.recovery_password_input import RecoveryPassword
from app.models.inputs.reste_password_input import ResetPassword
from app.services.user_manager import UserManager

user_router = APIRouter()


@user_router.post("/login")
@inject
async def login(
    data: LoginInput,
    manager: UserManager = Depends(get_user_manager),
):
    return manager.login(data)


@user_router.post("/password/recovery", status_code=status.HTTP_202_ACCEPTED)
@inject
async def password_recovery(
    data: RecoveryPassword,
    manager: UserManager = Depends(get_user_manager),
):
    manager.password_recovery(data)
    return {}


@user_router.post("/password/reset", status_code=status.HTTP_202_ACCEPTED)
@inject
async def password_reset(
    data: ResetPassword,
    manager: UserManager = Depends(get_user_manager),
):
    manager.password_reset(data)
    return {}
