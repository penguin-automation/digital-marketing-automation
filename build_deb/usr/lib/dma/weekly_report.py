import pandas as pd
from datetime import datetime
from loguru import logger
import os

# Log file path
log_file = "../logs/report_log.txt"
logger.add(log_file, format="{time} {level} {message}", level="INFO")

# Path data engagement
data_path = "../data/engagement_report.csv"

if not os.path.exists(data_path):
    logger.error("❌ File engagement_report.csv tidak ditemukan!")
    exit()

logger.info("📊 Membaca data engagement...")

data = pd.read_csv(data_path)
summary = data.describe()

# Buat folder report kalau belum ada
report_dir = "../data/reports"
os.makedirs(report_dir, exist_ok=True)

# Simpan laporan mingguan
filename = f"{report_dir}/weekly_report_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
summary.to_csv(filename)

logger.info(f"✅ Laporan mingguan tersimpan: {filename}")
print(f"📁 Report saved: {filename}")
