#!/usr/bin/env python3
import os
import csv
import argparse
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# ----- Config: gunakan env vars biar gak nyimpen password di file -----
SENDER_EMAIL = os.environ.get("your account")
APP_PASSWORD = os.environ.get("16characters")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))

# ----- Base dir agar path selalu benar kapanpun dijalankan -----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(BASE_DIR, "campaign_templates", "email_template.txt")
LEADS_PATH = os.path.join(BASE_DIR, "data", "leads.csv")
LOG_PATH = os.path.join(BASE_DIR, "logs", "campaign_log.txt")

# ----- Argparse -----
parser = argparse.ArgumentParser(description="Send email campaign (Debianist CLI)")
parser.add_argument("--dry-run", action="store_true", help="Dry run: don't actually send emails, only print actions")
args = parser.parse_args()

# ----- Baca template (cek dulu eksistensi) -----
if not os.path.exists(TEMPLATE_PATH):
    print(f"Template not found: {TEMPLATE_PATH}")
    raise SystemExit(1)

with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
    EMAIL_TEMPLATE = f.read()

# ----- Baca leads -----
if not os.path.exists(LEADS_PATH):
    print(f"Leads file not found: {LEADS_PATH}")
    raise SystemExit(1)

with open(LEADS_PATH, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    leads = list(reader)

if len(leads) == 0:
    print("No leads found in leads.csv")
    raise SystemExit(0)

# ----- Validasi kredensial (untuk mode kirim) -----
if not args.dry_run:
    if not SENDER_EMAIL or not APP_PASSWORD:
        print("ERROR: SENDER_EMAIL or APP_PASSWORD env var not set. Use --dry-run to test without sending.")
        raise SystemExit(1)

# ----- Fungsi kirim email -----
def send_email(recipient, subject, body, dry_run=True):
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL if SENDER_EMAIL else "no-reply"
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    if dry_run:
        print(f"[DRY] Would send to {recipient}")
        return True

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient, msg.as_string())
        return True
    except Exception as e:
        print(f"SMTP error sending to {recipient}: {e}")
        return False

# ----- Loop leads dan kirim -----
subject = "Your Automation Journey Starts Here 🐧✨"
now = datetime.now().isoformat(sep=" ", timespec="seconds")

for row in leads:
    name = row.get("name", "").strip()
    email = row.get("email", "").strip()
    if not email:
        print(f"Skipping lead with no email: {row}")
        continue

    personalized = EMAIL_TEMPLATE.replace("{{name}}", name if name else "Friend")
    success = send_email(email, subject, personalized, dry_run=args.dry_run)

    # Logging
    with open(LOG_PATH, "a", encoding="utf-8") as lf:
        lf.write(f"[{now}] to={email} name={name} status={'OK' if success else 'FAILED'}\n")

    print(f"{'✅' if success else '❌'} {email} ({name})")
