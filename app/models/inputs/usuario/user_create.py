from pydantic import BaseModel, Field, EmailStr, field_validator
from enum import Enum


class EnumRol(str, Enum):
    usuario = "usuario"
    admin = "admin"


class UsuarioCreate(BaseModel):
    email: EmailStr = Field(..., description="Correo del usuario")
    personaId: str = Field(..., description="UUID de la persona asociada")
    rol: EnumRol = Field(..., description="Rol del usuario")

    @field_validator("email", mode="before")
    def custom_email_error(cls, v):
        try:
            EmailStr.validate(v)
        except Exception:
            raise ValueError("Email inválido")
        return v
