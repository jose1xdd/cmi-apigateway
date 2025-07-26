import logging
from dependency_injector import containers, providers
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
        modules=["app.routers.main_router",
                 "app.utils.decorators.role_check_decorator"])

    db_session = providers.Resource(get_db)

    repository_factory = providers.Factory(
        RepositoryFactory,
        db=db_session,
    )

    usuario_repository = providers.Factory(
        lambda factory: factory.get_repository(IUsuarioRepository),
        factory=repository_factory
    )

    code_repository = providers.Factory(
        lambda factory: factory.get_repository(IRecoveryCodeRepository),
        factory=repository_factory
    )

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

    manager = providers.Factory(
        Manager,
        logger=logger,
        usuario_repository=usuario_repository,
        jwt_service=jwt_service,
        hashing_service=hashing_service,
        email_service=email_service,
        code_repository=code_repository,
        client_personas=client_personas
    )

    middleware_auth = providers.Factory(
        MiddlewarAuth,
        jwt_service=jwt_service,
        hashing_service=hashing_service,
        logger=logger
    )
