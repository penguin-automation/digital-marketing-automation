#!/usr/bin/env python3
import os
import subprocess
from loguru import logger
from argparse import ArgumentParser
from datetime import datetime

logger.add(os.path.expanduser("~/automation_project/logs/system_run.log"))

# path dasar
BASE_DIR = os.path.expanduser("~/automation_project/scripts")

TASKS = {
    "analyze": "analyze_engagement.py",
    "visual": "generate_visual_report.py",
    "portfolio": "generate_portfolio.py",
    "email": "gmail_api_send.py"
}

def run_task(script_name, desc):
    logger.info(f"🚀 Menjalankan {desc}...")
    script_path = os.path.join(BASE_DIR, script_name)
    result = subprocess.run(["python3", script_path], capture_output=True, text=True)
    if result.returncode == 0:
        logger.success(f"✅ {desc} selesai tanpa error.")
        print(result.stdout)
    else:
        logger.error(f"❌ {desc} gagal: {result.stderr}")
    print("-" * 60)

if __name__ == "__main__":
    parser = ArgumentParser(description="🐧 Digital Marketing CLI Automation v3.0")
    parser.add_argument("--all", action="store_true", help="Jalankan semua task secara berurutan")
    parser.add_argument("--analyze", action="store_true", help="Analisis engagement data")
    parser.add_argument("--visual", action="store_true", help="Buat visual report PDF")
    parser.add_argument("--portfolio", action="store_true", help="Generate portfolio lengkap")
    parser.add_argument("--email", action="store_true", help="Kirim report via Gmail API")
    args = parser.parse_args()

    start = datetime.now()
    logger.info(f"📅 Mulai run otomatis pada {start.strftime('%Y-%m-%d %H:%M:%S')}")

    if args.all:
        for key, script in TASKS.items():
            run_task(script, key.capitalize())
    else:
        if args.analyze: run_task(TASKS["analyze"], "Analisis Engagement")
        if args.visual: run_task(TASKS["visual"], "Visualisasi Report")
        if args.portfolio: run_task(TASKS["portfolio"], "Pembuatan Portfolio")
        if args.email: run_task(TASKS["email"], "Kirim Email via Gmail API")

    logger.info("🎯 Semua proses selesai. Log tersimpan di ~/automation_project/logs/system_run.log\n")
