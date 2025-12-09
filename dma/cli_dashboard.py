import pandas as pd
import time
import os
from loguru import logger

data_path = os.path.expanduser("~/automation_project/data/engagement_report.csv")

def display_dashboard():
    os.system("clear")
    df = pd.read_csv(data_path)
    df["total"] = df["likes"] + df["comments"] + df["shares"]

    top_platform = df.loc[df["total"].idxmax(), "platform"]
    total_engagement = df["total"].sum()
    avg_engagement = df["total"].mean()

    print("🐧========================================🐧")
    print("         DIGITAL MARKETING DASHBOARD      ")
    print("🐧========================================🐧")
    print(f"📈 Total Engagement Keseluruhan : {total_engagement}")
    print(f"⭐ Rata-rata Engagement per Platform : {avg_engagement:.2f}")
    print(f"🔥 Platform Terbaik Saat Ini : {top_platform}")
    print("🐧========================================🐧\n")

    print(df[["platform", "likes", "comments", "shares", "total"]])
    print("\nTekan Ctrl + C untuk keluar...")

if __name__ == "__main__":
    logger.info("🖥️ Menjalankan CLI Dashboard Digital Marketing...")
    try:
        while True:
            display_dashboard()
            time.sleep(5)
    except KeyboardInterrupt:
        logger.info("🚪 Dashboard ditutup.")
