from typing import Dict
from fastapi import Request, Depends

from app.utils.decorators.role_check_decorator import require_roles
from app.utils.exceptions_handlers.models.error_response import AppException


def validar_email_admin(
    request: Request,
    claims: Dict = Depends(require_roles(["usuario"])),
    path_param_key: str = "user_email",
) -> bool:
    """
    Valida que el usuario autenticado solo pueda modificar sus propios datos,
    salvo que tenga rol 'admin', en cuyo caso puede modificar cualquier usuario.
    """
    role = claims.get("role")
    header_persona_id = claims.get("email")
    path_persona_id = request.path_params.get(path_param_key)

    if header_persona_id != path_persona_id and role != "admin":
        raise AppException(
            codigo_http=403,
            mensaje="No autorizado: rol inválido"
        )

    return True
