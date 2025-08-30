from typing import Optional
from pydantic import BaseModel

class PublicacionUpdate(BaseModel):
    titulo: Optional[str] = None
    contenido: Optional[str] = None
