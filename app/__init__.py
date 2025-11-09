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
from app.routers.parcialidad_router import parcialidad_router
from app.routers.index_router import index_router
from app.routers.reporte_router import reportes_router
from app.routers.reuniones_router import reunion_router
from app.routers.asistencia_router import asistencia_router
from app.routers.censo_router import censo_router

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
    app.include_router(familia_router, prefix="/cmi-apigateway/familias")
    app.include_router(parcialidad_router, prefix="/cmi-apigateway/parcialidad")
    app.include_router(index_router, prefix="/cmi-apigateway/index")
    app.include_router(reportes_router, prefix="/cmi-apigateway/reportes")
    app.include_router(reunion_router,prefix="/cmi-apigateway/reunion")
    app.include_router(asistencia_router,prefix="/cmi-apigateway/asistencia")
    app.include_router(censo_router,prefix="/cmi-apigateway/censo")
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
        # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
        allow_methods=["*"],
        allow_headers=["*"],          # Permitir todos los headers
    )
    return app
