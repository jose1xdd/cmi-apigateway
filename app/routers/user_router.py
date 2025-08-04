from dependency_injector.wiring import inject
from fastapi import APIRouter, Depends, status

from app.ioc.container import get_user_manager
from app.models.inputs.usuario.login_input import LoginInput
from app.models.inputs.usuario.recovery_password_input import RecoveryPassword
from app.models.inputs.usuario.reste_password_input import ResetPassword
from app.models.outputs.usuario.login_response import EstadoResponse, LoginResponse
from app.services.user_manager import UserManager

user_router = APIRouter(tags=["Usuario"])


@user_router.post("/login", response_model=LoginResponse)
@inject
async def login(
    data: LoginInput,
    manager: UserManager = Depends(get_user_manager),
):
    return manager.login(data)


@user_router.post("/password/recovery", status_code=status.HTTP_202_ACCEPTED, response_model=EstadoResponse)
@inject
async def password_recovery(
    data: RecoveryPassword,
    manager: UserManager = Depends(get_user_manager),
):
    manager.password_recovery(data)
    return EstadoResponse(estado="Exitoso", message="Código de recuperación enviado correctamente")


@user_router.post("/password/reset", status_code=status.HTTP_202_ACCEPTED, response_model=EstadoResponse)
@inject
async def password_reset(
    data: ResetPassword,
    manager: UserManager = Depends(get_user_manager),
):
    manager.password_reset(data)
    return EstadoResponse(estado="Exitoso", message="Contraseña temporal enviada al correo")
