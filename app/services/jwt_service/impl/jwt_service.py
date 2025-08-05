
import jwt
from app.services.jwt_service.interface.interface_jwt_service import IJwtService
from datetime import datetime, timedelta, timezone


class JwtService(IJwtService):

    def __init__(self, secret_key: str, algorithm: str, expires_in_minutes: int):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.expires_in_minutes = expires_in_minutes

    def create_jwt_token(self, email: str, role: str, persona_id: str) -> str:
        """
        Genera un token JWT con el email como claim.
        """
        now = datetime.now(timezone.utc)
        expire = now + timedelta(minutes=self.expires_in_minutes)

        payload = {
            # Claim: Subject (usualmente el identificador principal)
            "email": email,
            "persona_id": persona_id,
            "role": role,
            "exp": expire,              # Claim: Expiration
            "iat": now,                 # Claim: Issued at
        }

        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token

    def decode_jwt_token(self, token: str) -> dict:
        """
        Decodifica un token JWT y devuelve los claims.
        """
        try:
            payload = jwt.decode(token, self.secret_key,
                                 algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token expirado")
        except jwt.InvalidTokenError:
            raise ValueError("Token inválido")
