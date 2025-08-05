from pydantic import BaseModel, EmailStr, Field


class RecoveryPassword(BaseModel):
    email: EmailStr = Field(..., description="Correo electrónico válido del usuario")
