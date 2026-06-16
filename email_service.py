import smtplib
import os

from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_SENHA = os.getenv("EMAIL_SENHA")
EMAIL_DESTINO = os.getenv("EMAIL_DESTINO")


def enviar_email_denuncia(protocolo, tipo, email, relato):

    corpo = f"""
NOVA DENÚNCIA RECEBIDA

PROTOCOLO: {protocolo}

TIPO: {tipo}

EMAIL: {email}

RELATO:

{relato}
"""

    mensagem = MIMEText(corpo)

    mensagem["Subject"] = f"Nova Denúncia - {protocolo}"
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = EMAIL_DESTINO

    servidor = smtplib.SMTP("smtp.gmail.com", 587)

    servidor.starttls()

    servidor.login(
        EMAIL_REMETENTE,
        EMAIL_SENHA
    )

    servidor.send_message(mensagem)

    servidor.quit()
    