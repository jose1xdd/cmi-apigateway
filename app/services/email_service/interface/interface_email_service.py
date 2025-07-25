from abc import ABC, abstractmethod


class IEmailService(ABC):
    @abstractmethod
    def send_email_recovery_password(self, destinatary: str, code: str):
        pass

    @abstractmethod
    def send_email_reset_password(self, destinatary: str, password: str):
        pass
