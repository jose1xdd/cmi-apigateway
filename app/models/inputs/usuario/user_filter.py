from pydantic import BaseModel, EmailStr
from typing import Optional
from app.persistence.model.enum import EnumRol


class UsuarioFilter(BaseModel):
    email: Optional[EmailStr] = None
    personaId: Optional[str] = None
    rol: Optional[EnumRol] = None

    class Config:
        from_attributes = True  # Para mapear desde SQLAlchemy
