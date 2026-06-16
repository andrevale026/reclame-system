import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
EMAIL_SENHA = os.getenv("EMAIL_SENHA")
EMAIL_DESTINO = os.getenv("EMAIL_DESTINO")

mensagem = MIMEText("Teste de envio do Sistema Reclame")

mensagem["Subject"] = "Teste Sistema Reclame"
mensagem["From"] = EMAIL_REMETENTE
mensagem["To"] = EMAIL_DESTINO

try:
    servidor = smtplib.SMTP("smtp.gmail.com", 587)

    servidor.starttls()

    servidor.login(
        EMAIL_REMETENTE,
        EMAIL_SENHA
    )

    servidor.send_message(mensagem)

    servidor.quit()

    print("E-mail enviado com sucesso!")

except Exception as erro:
    print("Erro:")
    print(erro)