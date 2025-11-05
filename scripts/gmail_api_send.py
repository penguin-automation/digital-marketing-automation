import os
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from loguru import logger

# File path
BASE_DIR = os.path.expanduser("~/automation_project/scripts")
TOKEN_PATH = os.path.join(BASE_DIR, "token.json")
CLIENT_SECRET_PATH = os.path.join(BASE_DIR, "client_secret.json")

# Scope Gmail API
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

def authenticate_gmail():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, "w") as token:
            token.write(creds.to_json())
    return creds

def send_email_gmail_api(sender, to, subject, body):
    creds = authenticate_gmail()
    service = build("gmail", "v1", credentials=creds)

    message = MIMEMultipart()
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    message.attach(MIMEText(body, "plain"))

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    message_body = {"raw": raw}

    sent = service.users().messages().send(userId="me", body=message_body).execute()
    logger.success(f"✅ Email terkirim ke {to} (ID: {sent['id']})")

if __name__ == "__main__":
    logger.info("🚀 Mengirim email via Gmail API...")
    sender = "karanva7@gmail.com"  # ubah sesuai email lo
    receiver = "akenaldiooo@gmail.com"  # email penerima
    subject = "Test Gmail API via Debian CLI 🐧"
    body = (
        "Halo brokk!\n\n"
        "Email ini dikirim otomatis via Gmail API di sistem Debian CLI.\n"
        "Tanpa SMTP, tanpa stunnel — full API-based automation 😎🔥\n\n"
        "🐧 Salam Linux!"
    )

    send_email_gmail_api(sender, receiver, subject, body)
