from fastapi import APIRouter, Depends, Query, status
from fastapi.responses import JSONResponse

from app.ioc.container import get_user_manager
from app.models.inputs.usuario.login_input import LoginInput
from app.models.inputs.usuario.recovery_password_input import RecoveryPassword
from app.models.inputs.usuario.refresh_input import RefreshRequest
from app.models.inputs.usuario.reste_password_input import ResetPassword
from app.models.inputs.usuario.update_password import UpdatePassword
from app.models.inputs.usuario.user_create import UsuarioCreate
from app.models.inputs.usuario.user_filter import UsuarioFilter
from app.models.inputs.usuario.user_update import UsuarioUpdate
from app.models.outputs.paginated_response import PaginatedUsuario
from app.models.outputs.response_estado import EstadoResponse
from app.models.outputs.usuario.login_response import LoginResponse
from app.models.outputs.usuario.usuario_output import UsuarioOut
from app.services.user_manager import UserManager
from app.utils.constans import BEARER_SCHEME
from app.utils.decorators.role_check_decorator import require_roles
from app.utils.decorators.validate_persona_admin import validar_email_admin

user_router = APIRouter(tags=["Usuario"])


@user_router.post("/login", response_model=LoginResponse)
async def login(
    data: LoginInput,
    manager: UserManager = Depends(get_user_manager),
):
    return manager.login(data)


@user_router.patch("/{user_email}/password/update", response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def update_password(
    data: UpdatePassword,
    user_email: str,
    _: bool = Depends(validar_email_admin),
    manager: UserManager = Depends(get_user_manager),
):
    response = manager.update_password(user_email, data)
    return JSONResponse(content=response.model_dump(exclude_none=True), status_code=200)


@user_router.post("/refresh", response_model=LoginResponse)
async def refresh(
    data: RefreshRequest,
    manager: UserManager = Depends(get_user_manager)
):
    return JSONResponse(content=manager.refresh_token(data.refresh_token))


@user_router.post("/password/recovery", status_code=status.HTTP_202_ACCEPTED, response_model=EstadoResponse)
async def password_recovery(
    data: RecoveryPassword,
    manager: UserManager = Depends(get_user_manager),
):
    manager.password_recovery(data)
    return EstadoResponse(estado="Exitoso", message="Código de recuperación enviado correctamente")


@user_router.post("/password/reset", status_code=status.HTTP_202_ACCEPTED, response_model=EstadoResponse)
async def password_reset(
    data: ResetPassword,
    manager: UserManager = Depends(get_user_manager),
):
    manager.password_reset(data)
    return EstadoResponse(estado="Exitoso", message="Contraseña temporal enviada al correo")


@user_router.post("/create", status_code=status.HTTP_201_CREATED, response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def create(
    data: UsuarioCreate,
    _: dict = Depends(require_roles([])),
    manager: UserManager = Depends(get_user_manager)
):
    response = manager.create_user(data)
    return JSONResponse(content=response.model_dump(exclude_none=True), status_code=201)


@user_router.delete("/delete/{email}", status_code=status.HTTP_200_OK, response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
async def delete(
    email: str,
    _: dict = Depends(require_roles([])),
    manager: UserManager = Depends(get_user_manager)
):
    response = manager.delete_user(email)
    return JSONResponse(content=response.model_dump(exclude_none=True), status_code=200)


@user_router.get("/", response_model=PaginatedUsuario, dependencies=[Depends(BEARER_SCHEME)])
def get_usuario(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, le=100),
    filters: UsuarioFilter = Depends(),
    _: dict = Depends(require_roles(["usuario"])),
    manager: UserManager = Depends(get_user_manager)
):
    return manager.get_user_filter(page, page_size, filters.model_dump(exclude_none=True))


@user_router.get("/{user_email}", response_model=UsuarioOut, dependencies=[Depends(BEARER_SCHEME)])
def get_personas(
    user_email: str,
    _: dict = Depends(require_roles(["usuario"])),
    manager: UserManager = Depends(get_user_manager)
):
    return manager.get_user_by_email(user_email)


@user_router.put("/{user_email}", response_model=EstadoResponse, dependencies=[Depends(BEARER_SCHEME)])
def update_user(
        user_email: str,
        data: UsuarioUpdate,
        _: bool = Depends(validar_email_admin),
        manager: UserManager = Depends(get_user_manager)):
    return manager.update_user(user_email, data)
