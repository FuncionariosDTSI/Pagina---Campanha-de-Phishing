import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Carregar a lista de e-mails de um arquivo CSV
# Assumindo um CSV com a coluna 'email'
email_list = pd.read_csv('C:/Users/Vinny/Documents/Python/Campanha de Phishing Simulado/email_list.csv')


# Configurações do servidor SMTP (exemplo usando Gmail)
SMTP_SERVER = "smtp.emailemnuvem.com.br"
SMTP_PORT = 587
SENDER_EMAIL = "ti@amadomaker.com"
SENDER_PASSWORD = "@2d=1h-6"

# Função para enviar e-mails
def send_phishing_email(receiver_email):
    try:
        # Criar o e-mail
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver_email
        msg['Subject'] = "Atualização de Senha Necessária"

        # Corpo do e-mail (simulado de phishing)
        body = """
        Prezado Colaborador,

        Para garantir a segurança da sua conta, clique no link abaixo para atualizar sua senha:
        <a href="http://localhost:8080/atualizar-senha">Atualizar Senha</a>

        Atenciosamente,
        Equipe de Segurança
        """
        msg.attach(MIMEText(body, 'html'))

        # Conectar ao servidor SMTP e enviar o e-mail
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, receiver_email, text)
        server.quit()

        print(f"E-mail enviado para {receiver_email}")
    except Exception as e:
        print(f"Falha ao enviar e-mail para {receiver_email}: {e}")

# Enviar e-mails para todos na lista
for email in email_list['email']:
    send_phishing_email(email)
