#!/usr/bin/env python3
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from loguru import logger
from datetime import datetime
import glob

# Direktori queue
QUEUE_DIR = os.path.expanduser("~/automation_project/data/email_queue")
REPORT_DIR = os.path.expanduser("~/automation_project/data/reports")
os.makedirs(QUEUE_DIR, exist_ok=True)

# Ambil env var
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

# Konfigurasi penerima
RECIPIENT = "client@example.com"
SUBJECT = "📊 Digital Marketing Report"

def send_email(file_path):
    """Kirim email atau simpan ke queue jika gagal"""
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT
    msg["Subject"] = SUBJECT

    body = f"Halo 👋,\n\nTerlampir laporan otomatis digital marketing.\n\nSalam,\nAkanra Debian CLI 🐧"
    msg.attach(MIMEText(body, "plain"))

    # lampirkan file
    with open(file_path, "rb") as f:
        part = MIMEText(f.read(), "base64", "utf-8")
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(file_path)}")
        msg.attach(part)

    try:
        logger.info("📡 Menghubungkan ke smtp.gmail.com:465 ...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        logger.success(f"✅ Email terkirim: {file_path}")
        return True
    except Exception as e:
        logger.warning(f"⚠️ Gagal kirim email ({e}), menyimpan ke queue...")
        queue_path = os.path.join(QUEUE_DIR, f"queued_{datetime.now().strftime('%Y%m%d_%H%M')}.txt")
        with open(queue_path, "w") as f:
            f.write(file_path)
        logger.info(f"📦 Disimpan ke queue: {queue_path}")
        return False

def resend_queued_emails():
    """Coba kirim ulang email yang ada di queue"""
    queued_files = glob.glob(os.path.join(QUEUE_DIR, "queued_*.txt"))
    if not queued_files:
        logger.info("📭 Tidak ada email di queue.")
        return

    logger.info(f"📨 Mencoba kirim ulang {len(queued_files)} email di queue...")
    for qf in queued_files:
        with open(qf, "r") as f:
            path = f.read().strip()
        if send_email(path):
            os.remove(qf)
            logger.success(f"🗑️ Email queue {os.path.basename(qf)} terkirim dan dihapus.")
        else:
            logger.warning(f"📌 Email {os.path.basename(qf)} masih gagal.")

if __name__ == "__main__":
    logger.info("📤 Auto Email Queue System Debian dimulai...")

    # cari laporan terbaru
    reports = sorted(glob.glob(os.path.join(REPORT_DIR, "*.pdf")), reverse=True)
    if reports:
        latest_report = reports[0]
        send_email(latest_report)
    else:
        logger.warning("⚠️ Tidak ada file laporan untuk dikirim.")

    resend_queued_emails()

