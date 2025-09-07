import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.services.email_service.interface.interface_email_service import IEmailService
from app.utils.email_templates import (
    PASSWORD_RECOVERY_TEMPLATE,
    TEMPORARY_PASSWORD_TEMPLATE,
    USER_CREATION_TEMPLATE,
)


class EmailService(IEmailService):
    def __init__(
        self,
        logger: logging.Logger,
        smtp_server: str,
        smtp_port: int,
        smtp_password: str,
        smtp_email: str,
    ):
        self.logger = logger
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_password = smtp_password
        self.smtp_email = smtp_email

    def _build_message(self, destinatary: str, subject: str, body_html: str) -> MIMEMultipart:
        """Construye el mensaje con HTML."""
        message = MIMEMultipart("alternative")
        message["From"] = self.smtp_email
        message["To"] = destinatary
        message["Subject"] = subject
        message.attach(MIMEText(body_html, "html"))
        return message

    def _send(self, destinatary: str, message: MIMEMultipart):
        """Envía el mensaje usando SMTP."""
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_email, self.smtp_password)
                server.sendmail(self.smtp_email, destinatary, message.as_string())

            self.logger.info(f"Correo enviado a: {destinatary}")
        except Exception as e:
            self.logger.error(f"Error al enviar correo a {destinatary}: {e}")
            raise

    def send_email_recovery_password(self, destinatary: str, code: str):
        """Envía correo de recuperación de contraseña con código."""
        body_html = PASSWORD_RECOVERY_TEMPLATE.replace("{{codigo}}", code)
        message = self._build_message(destinatary, "Reestablecer Contraseña", body_html)
        self._send(destinatary, message)

    def send_email_reset_password(self, destinatary: str, password: str):
        """Envía correo con contraseña provisional."""
        body_html = TEMPORARY_PASSWORD_TEMPLATE.replace("{{password}}", password)
        message = self._build_message(destinatary, "Contraseña Provisional", body_html)
        self._send(destinatary, message)

    def send_email_create(self, destinatary: str, password: str):
        """Nuevo método: Notifica creación de usuario con contraseña provisional."""
        body_html = USER_CREATION_TEMPLATE.replace("{{password}}", password)
        message = self._build_message(destinatary, "Bienvenido - Cuenta Creada", body_html)
        self._send(destinatary, message)
