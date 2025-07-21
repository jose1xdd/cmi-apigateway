from typing import TypedDict, Literal

class TokenClaimsDict(TypedDict):
    email: str
    role: Literal["admin", "user", "soporte"]  # o simplemente str
    exp: int
    iat: int
