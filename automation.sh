#!/bin/bash
# ==========================================================
# 🐧 Debian Freelancer Marketing Workflow
# ==========================================================

LOG_FILE="logs/campaign_log.txt"
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] 🚀 Starting daily automation..." >> $LOG_FILE

# 1️⃣ Kirim Email Campaign
echo "[$DATE] 📧 Sending email campaign..." >> $LOG_FILE
python3 dma/send_email.py --dry-run >> $LOG_FILE 2>&1

# 2️⃣ Posting ke Sosial Media (simulasi)
echo "[$DATE] 📱 Posting to social media..." >> $LOG_FILE
python3 dma/post_to_social.py --simulate >> $LOG_FILE 2>&1

# 3️⃣ Analisis Engagement
echo "[$DATE] 📊 Running engagement analysis..." >> $LOG_FILE
python3 dma/analyze_engagement.py --metric likes >> $LOG_FILE 2>&1

echo "[$DATE] ✅ Workflow completed successfully." >> $LOG_FILE
echo "=========================================================="
