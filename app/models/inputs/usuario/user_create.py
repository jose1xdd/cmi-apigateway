from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from enum import Enum


class EnumRol(str, Enum):
    usuario = "usuario"
    admin = "admin"


class UsuarioCreate(BaseModel):
    email: EmailStr = Field(..., max_length=100,
                            description="Correo del usuario")
    personaId: str = Field(..., description="UUID de la persona asociada")
    rol: EnumRol = Field(..., description="Rol del usuario")
