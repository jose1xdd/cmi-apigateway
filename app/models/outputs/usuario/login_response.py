from pydantic import BaseModel
from typing import Optional


class LoginResponse(BaseModel):
    estado: str
    jwt: Optional[str] = None
    refresh_token: Optional[str] = None

    class Config:
        exclude_none = True
