from pydantic import BaseModel, EmailStr, Field


class ResetPassword(BaseModel):
    email: EmailStr = Field(...,
                            description="Correo electrónico válido del usuario")
    code: str = Field(..., description="codigo de recuperacion")
