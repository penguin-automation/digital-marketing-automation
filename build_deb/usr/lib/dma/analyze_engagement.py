#!/usr/bin/env python3
import csv
import argparse
from statistics import mean

DATA_PATH = "../data/engagement_report.csv"

def analyze_engagement(metric="likes"):
    data = []
    with open(DATA_PATH, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                data.append(float(row[metric]))
            except (KeyError, ValueError):
                continue
    if not data:
        print(f"Tidak ada data valid untuk metrik '{metric}' 😅")
        return
    print(f"📈 Analisis untuk metrik: {metric}")
    print(f"  Rata-rata: {mean(data):.2f}")
    print(f"  Maksimum : {max(data):.2f}")
    print(f"  Minimum  : {min(data):.2f}")

def main():
    parser = argparse.ArgumentParser(description="CLI Engagement Analyzer 🐧")
    parser.add_argument("--metric", default="likes", help="Kolom metrik (likes, comments, shares, dsb.)")
    args = parser.parse_args()
    analyze_engagement(args.metric)

if __name__ == "__main__":
    main()
