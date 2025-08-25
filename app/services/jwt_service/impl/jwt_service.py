
import jwt
from app.services.jwt_service.interface.interface_jwt_service import IJwtService
from datetime import datetime, timedelta, timezone


class JwtService(IJwtService):

    def __init__(self, secret_key: str, algorithm: str, access_expires_minutes: int, refresh_expires_days: int):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.refresh_expires_days = refresh_expires_days
        self.access_expires_minutes = access_expires_minutes

    def create_jwt_token(self, email: str, role: str, persona_id: str) -> str:
        """
        Genera un token JWT con el email como claim.
        """
        now = datetime.now(timezone.utc)
        expire = now + timedelta(minutes=self.access_expires_minutes)

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

    def create_refresh_token(self, email: str, persona_id: str, role: str) -> str:
        """
        Genera un Refresh Token JWT con expiración más larga.
        """
        now = datetime.now(timezone.utc)
        expire = now + timedelta(days=self.refresh_expires_days)

        payload = {
            "email": email,
            "persona_id": persona_id,
            "role": role,
            "exp": expire,
            "iat": now,
            "type": "refresh"
        }

        token = jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
        return token

    def refresh_access_token(self, refresh_token: str) -> str:
        """
        Genera un nuevo Access Token a partir de un Refresh Token válido.
        """
        try:
            payload = self.decode_jwt_token(refresh_token)

            # Validar que sea un refresh token
            if payload.get("type") != "refresh":
                raise ValueError(
                    "El token proporcionado no es un refresh token")

            email = payload["email"]
            persona_id = payload["persona_id"]
            role = payload["role"]
            # Crear un nuevo access token
            new_access_token = self.create_jwt_token(
                email, role, persona_id)
            return new_access_token

        except Exception as e:
            raise ValueError(f"Error al refrescar el access token: {str(e)}")

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
