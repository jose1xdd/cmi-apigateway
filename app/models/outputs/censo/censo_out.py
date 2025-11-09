from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from datetime import date, datetime
from app.persistence.model.enum import EstadoCensoProceso


class CensoProcesoOut(BaseModel):
    id: int
    anio: int
    usuario: str
    estado: EstadoCensoProceso
    mensaje: Optional[str]
    fecha_inicio: datetime
    fecha_fin: Optional[datetime]

    class Config:
            from_attributes = True  # Permite mapear desde SQLAlchemy

class CensoAnualExcelOut(BaseModel):
    anio: int
    personaIdOrigen: Optional[str]
    tipoDocumento: Optional[str]
    numeroDocumento: Optional[str]
    nombre: Optional[str]
    apellido: Optional[str]
    fechaNacimiento: Optional[date]
    parentesco: Optional[str]
    sexo: Optional[str]
    profesion: Optional[str]
    escolaridad: Optional[str]
    direccion: Optional[str]
    telefono: Optional[str]
    fechaDefuncion: Optional[date]
    familiaIdOrigen: Optional[int]
    familiaEstado: Optional[str]
    familiaRepresentanteIdOrigen: Optional[str]
    familiaRepresentanteNombre: Optional[str]
    parcialidadNombre: Optional[str]

    class Config:
            from_attributes = True  # Permite mapear desde SQLAlchemy
