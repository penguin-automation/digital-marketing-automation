from __future__ import print_function
import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from loguru import logger

# ====== KONFIGURASI PATH RAHASIA (BARU) ======
HOME = os.path.expanduser("~")
CREDENTIAL_DIR = os.path.join(HOME, "Documents", "credentials")

CLIENT_SECRET_PATH = os.path.join(CREDENTIAL_DIR, "client_secret.json")
TOKEN_PATH = os.path.join(CREDENTIAL_DIR, "token.json")

# ====== GMAIL SCOPES ======
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def authenticate_gmail():
    """Autentikasi Gmail API menggunakan OAuth2"""
    creds = None

    # Coba pakai token.json
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    # Jika token kosong atau expired → login ulang
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_PATH, SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Simpan token baru
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())

    return creds


def send_email_gmail_api(sender, to, subject, body):
    logger.info("🚀 Mengirim email via Gmail API...")

    creds = authenticate_gmail()
    service = build("gmail", "v1", credentials=creds)

    message = MIMEText(body)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    sent = (
        service.users()
        .messages()
        .send(userId="me", body={"raw": raw_message})
        .execute()
    )

    logger.success(f"✅ Email terkirim ke {to} (ID: {sent['id']})")

if __name__ == "__main__":
    sender = "karanva7@gmail.com"
    receiver = "akenaldiooo@gmail.com"
    subject = "Test Email via Gmail API"
    body = "Hola brokk 🐧😆 — this is a test email via Gmail API!"

    send_email_gmail_api(sender, receiver, subject, body)
