
from typing import Optional
from pydantic import BaseModel


class PublicacionFilter(BaseModel):
    titulo: Optional[str] = None
