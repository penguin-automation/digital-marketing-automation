#!/usr/bin/env python3
import os
import time
import schedule
import subprocess
from datetime import datetime
from loguru import logger

# === Konfigurasi Path ===
BASE_DIR = os.path.expanduser("~/automation_project")
LOG_PATH = os.path.join(BASE_DIR, "logs/scheduler_log.txt")

# === Konfigurasi Logging ===
logger.add(LOG_PATH, rotation="1 day", format="{time} | {level} | {message}")

def run_script(script_path, desc):
    """Jalankan script Python eksternal"""
    full_path = os.path.join(BASE_DIR, script_path)
    if os.path.exists(full_path):
        logger.info(f"Menjalankan {desc} → {script_path}")
        try:
            subprocess.run(["python3", full_path], check=True)
            logger.success(f"{desc} selesai!")
        except subprocess.CalledProcessError as e:
            logger.error(f"Gagal menjalankan {desc}: {e}")
    else:
        logger.warning(f"File tidak ditemukan: {script_path}")

# === Jadwal Otomatis ===
def schedule_tasks():
    # Kirim email otomatis tiap jam
    schedule.every().hour.at(":00").do(run_script, "scripts/send_email.py", "Kirim Email Marketing")
    
    # Analisis engagement tiap 2 jam
    schedule.every(2).hours.at(":15").do(run_script, "scripts/analyze_engagement.py", "Analisis Engagement")

    # Log status tiap 30 menit
    schedule.every(30).minutes.do(lambda: logger.info("⏱️ Scheduler aktif — semua sistem aman."))

# === Main Loop ===
if __name__ == "__main__":
    logger.info("🚀 Scheduler Digital Marketing dimulai!")
    schedule_tasks()
    while True:
        schedule.run_pending()
        time.sleep(30)

import subprocess
import schedule
import time
from loguru import logger

# Jalankan modul laporan mingguan
def generate_weekly_report():
    logger.info("🗓️ Menjalankan generate laporan mingguan otomatis...")
    subprocess.run(["python3", "../scripts/weekly_report.py"])
    logger.info("✅ Laporan mingguan berhasil dibuat.")

# Jadwalkan tiap 7 hari sekali
schedule.every(7).days.do(generate_weekly_report)

logger.info("🕒 Scheduler siap menjalankan laporan mingguan otomatis...")

while True:
    schedule.run_pending()
    time.sleep(60)

import subprocess
import schedule
import time
from loguru import logger

# Log file path
log_file = "../logs/scheduler_log.txt"
logger.add(log_file, format="{time} | {level} | {message}", level="INFO")

# Jalankan modul laporan mingguan
def generate_weekly_report():
    logger.info("🗓️ Menjalankan generate laporan mingguan otomatis...")
    try:
        subprocess.run(["python3", "../scripts/weekly_report.py"], check=True)
        logger.success("✅ Laporan mingguan berhasil dibuat.")
    except subprocess.CalledProcessError:
        logger.error("❌ Gagal membuat laporan mingguan.")

# Jadwalkan tiap 7 hari sekali
schedule.every(7).days.do(generate_weekly_report)

logger.info("🕒 Scheduler siap menjalankan laporan mingguan otomatis...")

while True:
    schedule.run_pending()
    time.sleep(60)
