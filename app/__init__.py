import logging
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from app.ioc.container import Container
from app.utils.exceptions_handlers.exceptions_handlers import (
    custom_app_exception_handler,
    global_exception_handler,
    validation_exception_handler,
)
from app.utils.exceptions_handlers.models.error_response import AppException
from app.routers.user_router import user_router
from app.routers.persona_router import persona_router
from app.routers.familia_router import familia_router


def create_app() -> FastAPI:
    app = FastAPI()

    # Crear el container
    container = Container()
    container.wire(
        modules=[
            "app.ioc.container",
            "app.middlewares.middleware_auth",
            "app.utils.decorators.role_check_decorator"
        ]
    )
    app.container = container

    # Registrar excepciones
    app.add_exception_handler(AppException, custom_app_exception_handler)
    app.add_exception_handler(RequestValidationError,
                              validation_exception_handler)
    app.add_exception_handler(Exception, global_exception_handler)

    # Registrar router
    app.include_router(user_router, prefix="/cmi-apigateway")
    app.include_router(persona_router, prefix="/cmi-apigateway/personas")
    app.include_router(familia_router,prefix="/cmi-apigateway/familias")
    # Logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,        # Permitir todos los orígenes
        allow_credentials=True,
        allow_methods=["*"],          # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
        allow_headers=["*"],          # Permitir todos los headers
    )
    return app
