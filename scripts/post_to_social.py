#!/usr/bin/env python3
import argparse
import datetime
import os
import time

LOG_PATH = "../logs/campaign_log.txt"
TEMPLATE_PATH = "../campaign_templates/social_post_template.md"

def simulate_post(platform, message):
    print(f"📣 Posting ke {platform}...")
    time.sleep(1.2)
    print(f"✅ {platform}: Post berhasil — \"{message[:50]}...\"")

def main():
    parser = argparse.ArgumentParser(description="CLI Social Media Poster - Anak Debian Edition 🐧")
    parser.add_argument("--platforms", nargs="+", default=["Twitter", "LinkedIn"], help="List platform")
    parser.add_argument("--dry-run", action="store_true", help="Simulasi tanpa posting sungguhan")
    args = parser.parse_args()

    if not os.path.exists(TEMPLATE_PATH):
        print(f"Template tidak ditemukan di {TEMPLATE_PATH}")
        return

    with open(TEMPLATE_PATH, "r") as f:
        message = f.read().strip()

    for platform in args.platforms:
        if args.dry_run:
            print(f"[DRY] Akan posting ke {platform}: \"{message[:60]}...\"")
        else:
            simulate_post(platform, message)

    with open(LOG_PATH, "a") as log:
        log.write(f"[{datetime.datetime.now()}] Posted to {', '.join(args.platforms)}\n")

    print("\n📝 Log tercatat di logs/campaign_log.txt")

if __name__ == "__main__":
    main()
