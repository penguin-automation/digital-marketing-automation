#!/usr/bin/env python3
import os
import smtplib
import argparse
from email.message import EmailMessage
from datetime import datetime
from loguru import logger

# ==============================
# Konfigurasi Awal
# ==============================
REPORT_DIR = os.path.expanduser("~/automation_project/data/reports")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECEIVER_EMAIL = "akenaldiooo@gmail.com"  # ubah sesuai target
SUBJECT = "📈 Digital Marketing Portfolio Update"

# ==============================
# Cari File PDF Terbaru
# ==============================
def get_latest_report():
    pdfs = sorted(
        [f for f in os.listdir(REPORT_DIR) if f.endswith(".pdf")],
        key=lambda x: os.path.getmtime(os.path.join(REPORT_DIR, x)),
        reverse=True,
    )
    if pdfs:
        return os.path.join(REPORT_DIR, pdfs[0])
    else:
        logger.warning("⚠️ Tidak ada file PDF yang ditemukan di reports/")
        return None

# ==============================
# Kirim Email
# ==============================
def send_email(dry_run=False):
    if not SENDER_EMAIL or not APP_PASSWORD:
        logger.error("⚠️ SENDER_EMAIL / APP_PASSWORD belum di-set di environment.")
        return

    latest_report = get_latest_report()
    if not latest_report:
        logger.error("❌ Gagal menemukan laporan untuk dikirim.")
        return

    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = SUBJECT
    msg.set_content(
        f"""
Halo klien,

Berikut laporan digital marketing otomatis dari sistem Debian CLI 🐧✨
Tanggal: {datetime.now().strftime("%d %B %Y, %H:%M")}

Silakan cek file terlampir untuk portofolio lengkap.
Salam,
Akanra – Digital Marketing Automation (Debian Edition)
        """
    )

    # Lampirkan file PDF
    with open(latest_report, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=os.path.basename(latest_report),
        )

    if dry_run:
        logger.success(f"[DRY-RUN] Email siap dikirim dari {SENDER_EMAIL} ke {RECEIVER_EMAIL}")
        return

    # ==============================
    # Koneksi Email
    # ==============================
    try:
        logger.info("📡 Mencoba koneksi SSL ke smtp.gmail.com:465 ...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        logger.success("✅ Email terkirim sukses via SSL!")
    except Exception as e:
        logger.warning(f"⚠️ SSL gagal: {e}, mencoba fallback TLS...")
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.ehlo()
                server.starttls()
                server.login(SENDER_EMAIL, APP_PASSWORD)
                server.send_message(msg)
            logger.success("✅ Email terkirim sukses via TLS (fallback)!")
        except Exception as e2:
            logger.error(f"❌ Gagal mengirim email: {e2}")

# ==============================
# Main
# ==============================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Test tanpa kirim email.")
    args = parser.parse_args()

    logger.info("📤 Mengirim laporan otomatis via email...")
    send_email(dry_run=args.dry_run)

