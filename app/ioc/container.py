import logging
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from requests import Session
from app.client.ms_gestion_usuarios.impl.client_personas import ClientPersonas
from app.config.database import get_db
from app.middlewares.middleware_auth import MiddlewarAuth
from app.persistence.repository.recovery_code_repository.interface.interface_recovery_code_repository import IRecoveryCodeRepository
from app.persistence.repository.repository_factory import RepositoryFactory
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository
from app.services.email_service.impl.email_service import EmailService
from app.services.hashing_service.impl.hashing_service import HashingService
from app.services.jwt_service.impl.jwt_service import JwtService
from app.services.manager import Manager
from app.utils.enviroment import settings


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=["app.ioc.container",
                 "app.utils.decorators.role_check_decorator"])

    logger = providers.Singleton(logging.getLogger, __name__)

    hashing_service = providers.Factory(
        HashingService
    )

    jwt_service = providers.Factory(
        JwtService,
        expires_in_minutes=settings.expires_in_minutes,
        algorithm=settings.algorithm,
        secret_key=settings.secret_key
    )

    email_service = providers.Factory(
        EmailService,
        logger=logger,
        smtp_server=settings.smtp_server,
        smtp_port=settings.smtp_port,
        smtp_password=settings.smtp_password,
        smtp_email=settings.smtp_email
    )

    client_personas = providers.Factory(
        ClientPersonas,
        url=settings.ms_gestion_usuarios_url
    )

    middleware_auth = providers.Factory(
        MiddlewarAuth,
        jwt_service=jwt_service,
        hashing_service=hashing_service,
        logger=logger
    )


@inject
def get_manager(
    db: Session = Depends(get_db),
    logger: logging.Logger = Depends(Provide[Container.logger]),
    jwt_service=Depends(Provide[Container.jwt_service]),
    hashing_service=Depends(Provide[Container.hashing_service]),
    email_service=Depends(Provide[Container.email_service]),
    client_personas=Depends(Provide[Container.client_personas]),
) -> Manager:
    factory = RepositoryFactory(db=db)

    return Manager(
        logger=logger,
        usuario_repository=factory.get_repository(IUsuarioRepository),
        code_repository=factory.get_repository(IRecoveryCodeRepository),
        jwt_service=jwt_service,
        hashing_service=hashing_service,
        email_service=email_service,
        client_personas=client_personas
    )
