from pydantic import BaseModel, Field

class RefreshRequest(BaseModel):
    refresh_token: str = Field(..., description="Token de refresco JWT")
