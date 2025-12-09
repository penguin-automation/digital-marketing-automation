import pandas as pd
from datetime import datetime
from loguru import logger
import os
import random

file_path = os.path.expanduser("~/automation_project/data/engagement_report.csv")
output_file = os.path.expanduser(
    f"~/automation_project/data/reports/ai_insight_local_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
)

try:
    df = pd.read_csv(file_path)
    logger.info("📊 Membaca data engagement lokal...")

    best_platform = df.loc[df["likes"].idxmax(), "platform"]
    avg_like = df["likes"].mean()
    avg_comment = df["comments"].mean()
    avg_share = df["shares"].mean()

    style = [
        "optimis",
        "profesional",
        "data-driven",
        "tegas dan visioner",
        "santai tapi strategis",
    ]
    chosen_style = random.choice(style)

    insight = f"""
📈 [AI Insight Lokal – {datetime.now().strftime("%d %B %Y")}]

🔥 Platform paling populer: {best_platform}
💬 Rata-rata Likes: {avg_like:.2f}
💭 Rata-rata Comments: {avg_comment:.2f}
📣 Rata-rata Shares: {avg_share:.2f}

💡 Rekomendasi ({chosen_style}):
- Fokuskan produksi konten di platform {best_platform}.
- Tingkatkan kualitas interaksi melalui komentar aktif & storytelling ringan.
- Coba variasi posting jam prime time untuk hasil lebih maksimal.
- Gunakan automasi hashtag & respon cepat pelanggan.

🐧 Insight ini dihasilkan langsung dari sistem CLI Debian – tanpa API eksternal.
"""

    with open(output_file, "w") as f:
        f.write(insight.strip())

    logger.success(f"✅ Insight lokal tersimpan di {output_file}")
    print(insight)

except Exception as e:
    logger.error(f"Gagal menghasilkan insight lokal: {e}")
