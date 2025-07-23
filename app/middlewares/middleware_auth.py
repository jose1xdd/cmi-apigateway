import logging

from fastapi import Request
from app.services.hashing_service.interface.interface_hashing_service import IHashingService
from app.services.jwt_service.interface.interface_jwt_service import IJwtService
from fastapi import Request, status
from app.utils.constans import AUTH_HEADER
from app.utils.exceptions_handlers.models.error_response import AppException


class MiddlewarAuth():
    def __init__(self, jwt_service: IJwtService,
                 hashing_service: IHashingService,
                 logger: logging.Logger):
        self.logger = logger
        self.jwt_service = jwt_service
        self.hashing_service = hashing_service

    def validate_token(self, request: Request):
        self.logger.info("validando jwt")
        jwt = request.headers.get(AUTH_HEADER)
        if not jwt:
            raise AppException(
                codigo_http=status.HTTP_400_BAD_REQUEST,
                mensaje="Token no proporcionado"
            )
        jwt = jwt.replace("Bearer ", "")
        return self.jwt_service.decode_jwt_token(jwt)
