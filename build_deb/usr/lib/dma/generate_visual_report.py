import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from loguru import logger

# Direktori file
report_dir = os.path.expanduser("~/automation_project/data/reports")
engagement_file = os.path.expanduser("~/automation_project/data/engagement_report.csv")
output_pdf = os.path.join(report_dir, f"visual_portfolio_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf")

logger.info("🎨 Membuat visualisasi portofolio...")

try:
    # Baca data
    df = pd.read_csv(engagement_file)
    logger.info(f"📊 Data dimuat: {len(df)} baris")

    # Buat grafik batang
    plt.figure(figsize=(7, 4))
    plt.bar(df["platform"], df["likes"], color="skyblue", label="Likes")
    plt.bar(df["platform"], df["comments"], color="orange", bottom=df["likes"], label="Comments")
    plt.title("Engagement per Platform")
    plt.xlabel("Platform")
    plt.ylabel("Jumlah Interaksi")
    plt.legend()
    plt.tight_layout()

    chart_path = os.path.join(report_dir, "chart_temp.png")
    plt.savefig(chart_path)
    plt.close()

    # Buat PDF
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 18)
    c.drawString(100, height - 100, "📄 Visual Marketing Report")
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 130, f"Tanggal: {datetime.now().strftime('%d %B %Y')}")

    # Tambah chart ke PDF
    c.drawImage(ImageReader(chart_path), 80, height - 450, width=450, height=300)

    # Tambah summary
    avg_likes = df["likes"].mean()
    top_platform = df.loc[df["likes"].idxmax(), "platform"]
    summary = f"Platform terbaik: {top_platform} | Rata-rata Likes: {avg_likes:.1f}"

    c.setFont("Helvetica-Bold", 13)
    c.drawString(100, height - 480, "Summary:")
    c.setFont("Helvetica", 11)
    c.drawString(120, height - 500, summary)

    c.save()
    logger.success(f"✅ Visual Report tersimpan di {output_pdf}")
    print(f"\n📁 Report Generated: {output_pdf}")

except Exception as e:
    logger.error(f"Gagal membuat visualisasi: {e}")
