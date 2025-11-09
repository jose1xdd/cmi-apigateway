from pydantic import BaseModel, Field

class CensoGenerateIn(BaseModel):
    """
    Modelo de entrada para generar un censo anual.
    """
    anio: int = Field(..., ge=2000, le=2100, description="Año del censo a generar (por ejemplo, 2025)")
    usuario: str = Field(..., description="Usuario responsable que inicia el proceso del censo")
    esPrueba: bool = Field(default=False, description="Indica si el censo es de prueba o real")
