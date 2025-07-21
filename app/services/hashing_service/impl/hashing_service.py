import hashlib
from app.services.hashing_service.interface.interface_hashing_service import IHashingService


class HashingService(IHashingService):
    """
    Hashea una contraseña con SHA-256.
    """

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def verify_password(self, password: str, hashed_password: str) -> bool:
        """
        Compara una contraseña en texto plano con un hash SHA-256.
        """
        return password == hashed_password
