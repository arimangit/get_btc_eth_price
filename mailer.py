import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_email(recipient: str, subject: str, body: str):
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    email_from = os.getenv("EMAIL_FROM")

    msg = MIMEMultipart()
    msg["From"] = email_from
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(email_from, recipient, msg.as_string())

    print(f"Email sent to {recipient}")

def send_crypto_email(rates: dict, recipient: str = None, subject: str = "Crypto Price Update - BTC & ETH"):
    email_to = recipient or os.getenv("SMTP_USER")
    body = "\n".join(rates.values())
    send_email(email_to, subject, body)
