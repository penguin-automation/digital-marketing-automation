import pandas as pd
import os
from datetime import datetime
from loguru import logger

report_dir = os.path.expanduser("~/automation_project/data/reports")
data_dir = os.path.expanduser("~/automation_project/data")
output_file = os.path.join(report_dir, f"ai_insight_{datetime.now().strftime('%Y%m%d_%H%M')}.txt")

logger.info("🤖 Memulai analisis AI insight dari data engagement...")

def load_latest_report():
    """Coba baca weekly_report, kalau gagal fallback ke engagement_report.csv"""
    try:
        latest_file = sorted([f for f in os.listdir(report_dir) if f.startswith("weekly_report_")])[-1]
        path = os.path.join(report_dir, latest_file)
        logger.info(f"📂 Membaca file report: {path}")
        df = pd.read_csv(path)
        if 'platform' not in df.columns:
            raise KeyError("Kolom 'platform' tidak ditemukan")
        return df
    except Exception as e:
        logger.warning(f"⚠️ Gagal baca report mingguan: {e}, fallback ke engagement_report.csv")
        fallback = os.path.join(data_dir, "engagement_report.csv")
        df = pd.read_csv(fallback)
        return df

df = load_latest_report()

try:
    top_platform = df.loc[df['likes'].idxmax(), 'platform']
    avg_likes = df['likes'].mean()
    avg_comments = df['comments'].mean()
    avg_shares = df['shares'].mean()

    insight = f"""
📊 [AI INSIGHT - {datetime.now().strftime('%d %B %Y')}]

🔥 Platform paling populer minggu ini: {top_platform}
💬 Rata-rata Likes: {avg_likes:.2f}
💭 Rata-rata Comments: {avg_comments:.2f}
📣 Rata-rata Shares: {avg_shares:.2f}

💡 Rekomendasi:
- Fokuskan promosi di {top_platform} minggu depan.
- Coba tingkatkan interaksi komentar untuk engagement lebih tinggi.
    """

    with open(output_file, "w") as f:
        f.write(insight)

    logger.success(f"✅ Insight tersimpan di {output_file}")
    print(insight)
except Exception as e:
    logger.error(f"Gagal menghasilkan insight: {e}")

