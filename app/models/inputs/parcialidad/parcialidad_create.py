from pydantic import BaseModel


class ParcialidadCreate(BaseModel):
    nombre_parcialidad: str
    class Config:
        from_attributes = True  # Para convertir entre SQLAlchemy y Pydantic fácilmente
