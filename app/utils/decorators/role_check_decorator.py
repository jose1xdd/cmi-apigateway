from fastapi import Depends, HTTPException, Request, status
from typing import List
from dependency_injector.wiring import Provide, inject
from app.ioc.container import Container
from app.middlewares.middleware_auth import MiddlewarAuth
from app.services.jwt_service.models.token_claims_schema import TokenClaimsDict
from app.utils.exceptions_handlers.models.error_response import AppException


def require_roles(permitted_roles: List[str]):
    @inject
    def role_dependency(
        request: Request,
        auth: MiddlewarAuth = Depends(Provide[Container.middleware_auth])
    ):
        claims: TokenClaimsDict = auth.validate_token(request)
        user_role = claims.get("role")
        if user_role not in permitted_roles:
            raise AppException(
                codigo=status.HTTP_403_FORBIDDEN,
                mensaje="No tienes permiso para acceder a este recurso"
            )
        return claims
    return role_dependency
