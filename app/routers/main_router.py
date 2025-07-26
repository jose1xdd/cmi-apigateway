from dependency_injector.wiring import inject
from fastapi import APIRouter, Depends, Request, Response, status

from app.ioc.container import get_manager
from app.models.inputs.login_input import LoginInput
from app.models.inputs.recovery_password_input import RecoveryPassword
from app.models.inputs.reste_password_input import ResetPassword
from app.services.manager import Manager
from app.utils.decorators.role_check_decorator import require_roles

main_router = APIRouter()

@main_router.post("/login")
@inject
async def login(
    data: LoginInput,
    manager: Manager = Depends(get_manager),
):
    return manager.login(data)

@main_router.post("/password/recovery", status_code=status.HTTP_202_ACCEPTED)
@inject
async def password_recovery(
    data: RecoveryPassword,
    manager: Manager = Depends(get_manager),
):
    manager.password_recovery(data)
    return {}

@main_router.post("/password/reset", status_code=status.HTTP_202_ACCEPTED)
@inject
async def password_reset(
    data: ResetPassword,
    manager: Manager = Depends(get_manager),
):
    manager.password_reset(data)
    return {}

@main_router.post("/personas/create", status_code=status.HTTP_202_ACCEPTED)
@inject
async def create_persona(
    data: Request,
    claims: dict = Depends(require_roles(["admin"])),
    manager: Manager = Depends(get_manager),
):
    body = await data.json()
    external_response = manager.create_person(body)
    return Response(
        content=external_response.content,
        status_code=external_response.status_code,
        media_type=external_response.headers.get("Content-Type", "application/json"),
    )
