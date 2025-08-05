from abc import ABC, abstractmethod


class IJwtService(ABC):
    @abstractmethod
    def create_jwt_token(self, email: str, role: str, persona_id: str) -> str:
        pass

    @abstractmethod
    def decode_jwt_token(token: str) -> dict:
        pass
