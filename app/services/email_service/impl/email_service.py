import logging
from app.services.email_service.interface.interface_email_service import IEmailService

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.utils.email_templates import PASSWORD_RECOVERY_TEMPLATE, TEMPORARY_PASSWORD_TEMPLATE


class EmailService(IEmailService):
    def __init__(self, logger: logging.Logger,
                 smtp_server: str,
                 smtp_port: int,
                 smtp_password: str,
                 smtp_email: str):
        self.logger = logger
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_password = smtp_password
        self.smtp_email = smtp_email

    def send_email_recovery_password(self, destinatary: str, code: str):
        try:
            message = MIMEMultipart("alternative")
            message["From"] = self.smtp_email
            message["To"] = destinatary
            message["Subject"] = "Reestablecer Contraseña"
            body = PASSWORD_RECOVERY_TEMPLATE.replace("{{codigo}}", code)
            body_html = MIMEText(body, "html")
            message.attach(body_html)
            # Enviar el correo
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_email, self.smtp_password)
                server.sendmail(self.smtp_email, destinatary,
                                message.as_string())

            self.logger.info(
                f"Correo de recuperación enviado a: {destinatary}")

        except Exception as e:
            self.logger.error(f"Error al enviar correo: {e}")
            raise
    
    def send_email_reset_password(self, destinatary: str, password: str):
        try:
            message = MIMEMultipart("alternative")
            message["From"] = self.smtp_email
            message["To"] = destinatary
            message["Subject"] = "Contraseña Provicional"
            body = TEMPORARY_PASSWORD_TEMPLATE.replace("{{password}}", password)
            body_html = MIMEText(body, "html")
            message.attach(body_html)
            # Enviar el correo
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_email, self.smtp_password)
                server.sendmail(self.smtp_email, destinatary,
                                message.as_string())

            self.logger.info(
                f"Correo de recuperación enviado a: {destinatary}")

        except Exception as e:
            self.logger.error(f"Error al enviar correo: {e}")
            raise