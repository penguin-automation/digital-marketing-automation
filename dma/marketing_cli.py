#!/usr/bin/env python3
import os
import subprocess
from loguru import logger
from argparse import ArgumentParser
from datetime import datetime

# Log file
logger.add(os.path.expanduser("~/automation_project/logs/system_run.log"))

# Path modul package DMA
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mapping modul
TASKS = {
    "analyze": "dma.analyze_engagement",
    "visual": "dma.generate_visual_report",
    "portfolio": "dma.generate_portfolio",
    "email": "dma.gmail_api_send",
}

def run_task(module_path, desc):
    logger.info(f"🚀 Menjalankan {desc}...")
    result = subprocess.run(
        ["python3", "-m", module_path],
        capture_output=True,
        text=True
    )
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
        for key, module in TASKS.items():
            run_task(module, key.capitalize())
    else:
        if args.analyze: run_task(TASKS["analyze"], "Analisis Engagement")
        if args.visual: run_task(TASKS["visual"], "Visualisasi Report")
        if args.portfolio: run_task(TASKS["portfolio"], "Pembuatan Portfolio")
        if args.email: run_task(TASKS["email"], "Kirim Email via Gmail API")

    logger.info("🎯 Semua proses selesai. Log tersimpan di ~/automation_project/logs/system_run.log\n")

