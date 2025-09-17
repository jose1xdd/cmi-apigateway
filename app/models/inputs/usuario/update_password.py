from pydantic import BaseModel, EmailStr, Field


class UpdatePassword(BaseModel):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        description="Contraseña con mínimo 8 caracteres"
    )
