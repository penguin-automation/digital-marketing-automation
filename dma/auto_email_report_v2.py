#!/usr/bin/env python3
import os, smtplib, socket, argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from loguru import logger

def port_open(host, port, timeout=2):
    """Cek apakah port terbuka"""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False

def send_email(sender_email, app_password, recipient, subject, body, dry_run=False):
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # pilih koneksi otomatis
    connection_mode = None
    try:
        if port_open("smtp.gmail.com", 465):
            logger.info("📡 Menggunakan koneksi langsung SSL (465)")
            smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10)
            connection_mode = "SSL"
        elif port_open("smtp.gmail.com", 587):
            logger.info("📡 Menggunakan koneksi TLS (587)")
            smtp = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
            smtp.starttls()
            connection_mode = "TLS"
        elif port_open("127.0.0.1", 10443):
            logger.info("🧩 Menggunakan tunnel lokal via stunnel (port 443)")
            smtp = smtplib.SMTP_SSL("127.0.0.1", 10443, timeout=10)
            connection_mode = "TUNNEL"
        else:
            logger.error("❌ Tidak ada port SMTP yang bisa diakses (465/587/443)")
            return

        if dry_run:
            logger.success(f"[DRY-RUN] Email siap dikirim via mode {connection_mode} ke {recipient}")
            smtp.quit()
            return

        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
        smtp.quit()
        logger.success(f"✅ Email terkirim ke {recipient} (mode: {connection_mode})")

    except Exception as e:
        logger.error(f"🚨 Gagal mengirim email ({connection_mode}): {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="📤 Kirim laporan otomatis via email dengan fallback 443")
    parser.add_argument("--dry-run", action="store_true", help="Test mode tanpa kirim email")
    args = parser.parse_args()

    logger.info("🚀 Memulai Auto Email Report v2...")

    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    if not sender_email or not app_password:
        logger.error("⚠️ SENDER_EMAIL / APP_PASSWORD belum di-set di environment.")
        exit(1)

    recipient = "akenaldiooo@gmail.com"
    subject = "📊 Laporan Otomatis Digital Marketing"
    body = "Halo, ini laporan otomatis dari Debian CLI 🐧🔥"

    send_email(sender_email, app_password, recipient, subject, body, dry_run=args.dry_run)
