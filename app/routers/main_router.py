from fastapi import APIRouter, Depends
import logging
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.models.schemas.usuario_schema import UsuarioCreate
from app.persistence.repository.repository_factory import RepositoryFactory
from app.persistence.repository.user_repository.interface.interface_user_repository import IUsuarioRepository

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger_printer = logging.getLogger(__name__)

main_router = APIRouter()

@main_router.get("/login")
def login(db: Session = Depends(get_db)):
    usuario = UsuarioCreate(
        email="juan1.perez@example.com",
        password="secreto123",
        personaId="1234567890"
    )
    logger_printer.info("manfredo godofredo")
    usuario_repo = RepositoryFactory.get_repository(IUsuarioRepository, db)
    created_user = usuario_repo.create(usuario)
    return {"message": "Usuario creado", "user": created_user}