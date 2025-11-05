import os
import pandas as pd
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from loguru import logger

# === Konfigurasi dasar ===
report_dir = os.path.expanduser("~/automation_project/data/reports")
engagement_main = os.path.expanduser("~/automation_project/data/engagement_report.csv")
output_file = os.path.join(report_dir, f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf")

logger.info("📊 Membuat portofolio digital marketing...")

try:
    # === Cari file laporan terbaru ===
    reports = [f for f in os.listdir(report_dir) if f.startswith("weekly_report_")]
    reports.sort(reverse=True)
    latest_report = os.path.join(report_dir, reports[0]) if reports else engagement_main

    # === Baca data utama ===
    df = pd.read_csv(latest_report)
    if "platform" not in df.columns:
        logger.warning("⚠️ Kolom 'platform' tidak ditemukan — fallback ke engagement_report.csv")
        df = pd.read_csv(engagement_main)

    # === Siapkan canvas PDF ===
    c = canvas.Canvas(output_file, pagesize=A4)
    width, height = A4

    # === Header dokumen ===
    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, height - 100, "📄 Digital Marketing Portfolio Report")

    c.setFont("Helvetica", 12)
    c.drawString(100, height - 130, f"Tanggal: {datetime.now().strftime('%d %B %Y')}")

    # === Ringkasan Engagement ===
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, height - 170, "Engagement Summary:")
    y = height - 190

    for _, row in df.iterrows():
        text = f"- {row['platform']}: {row['likes']} Likes, {row['comments']} Comments, {row['shares']} Shares"
        c.setFont("Helvetica", 11)
        c.drawString(120, y, text)
        y -= 20
        if y < 100:
            c.showPage()
            y = height - 100

    # === Tambahkan AI Insight Lokal ===
    insight_files = [f for f in os.listdir(report_dir) if f.startswith("ai_insight_local_")]
    insight_files.sort(reverse=True)

    if insight_files:
        latest_insight = os.path.join(report_dir, insight_files[0])
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, y - 30, "AI Insight Lokal:")
        y -= 50

        with open(latest_insight, "r") as f:
            lines = f.readlines()
        for line in lines:
            c.setFont("Helvetica", 10)
            c.drawString(110, y, line.strip())
            y -= 14
            if y < 100:
                c.showPage()
                y = height - 100

    # === Tambahkan signature digital ===
    signature_text = (
        "---\n"
        "Generated automatically by Akanra’s Debian CLI Automation System 🐧✨\n"
        "All data processed locally using Python + Debian environment."
    )
    c.setFont("Helvetica-Oblique", 9)
    c.drawString(100, 80, signature_text)

    # === Simpan dan tutup PDF ===
    c.save()
    logger.success(f"✅ Portfolio lengkap tersimpan di {output_file}")
    print(f"\n📁 Portfolio Generated: {output_file}")

except Exception as e:
    logger.error(f"Gagal membuat portofolio lengkap: {e}")

