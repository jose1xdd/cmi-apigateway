from pydantic import BaseModel, EmailStr, Field

class LoginInput(BaseModel):
    email: EmailStr = Field(..., description="Correo electrónico válido del usuario")
    password: str = Field