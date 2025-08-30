import base64
from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class FotoOut(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)
    
class PublicacionOut(BaseModel):
    id: int
    titulo: Optional[str] = None
    contenido: Optional[str] = None
    fotos: List[FotoOut] = []

    model_config = ConfigDict(from_attributes=True)

    @classmethod
    def model_validate(cls, obj):
        """
        Valida publicación + transforma las fotos con Base64
        """
        return cls(
            id=obj.id,
            titulo=obj.titulo,
            contenido=obj.contenido,
            fotos=[FotoOut.model_validate(f) for f in obj.fotos]
        )
