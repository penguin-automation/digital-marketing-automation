#!/bin/bash
# ==========================================
# 🐧 Debian Automation CLI – Cheat Sheet 🧠
# ==========================================
# Dibuat oleh: Akanra (Automation Project)
# Tujuan: Panduan cepat semua perintah utama
# ==========================================

# === 1. Aktivasi Virtual Environment ===
echo "🔹 Mengaktifkan environment..."
source ~/venv/automation/bin/activate

# === 2. Jalankan Analisis Engagement ===
echo "🔹 Menjalankan analisis engagement..."
python3 ~/automation_project/scripts/analyze_ai_insight_local.py

# === 3. Generate Visual Report (PDF) ===
echo "🔹 Membuat visualisasi PDF report..."
python3 ~/automation_project/scripts/generate_visual_report.py

# === 4. Generate Portfolio Lengkap ===
echo "🔹 Membuat portofolio marketing..."
python3 ~/automation_project/scripts/generate_portfolio.py

# === 5. Dashboard Mini CLI ===
echo "🔹 Menampilkan dashboard digital marketing..."
python3 ~/automation_project/scripts/dashboard_cli.py

# === 6. Auto Email Report (Dry Run Mode) ===
echo "🔹 Menguji pengiriman email (dry-run)..."
SENDER_EMAIL="karanva7@gmail.com" APP_PASSWORD="ardnknrcljvsoqqs" python3 ~/automation_project/scripts/auto_email_report.py --dry-run

# === 7. Kirim Email Sungguhan via Gmail API ===
echo "🔹 Mengirim email via Gmail API..."
python3 ~/automation_project/scripts/gmail_api_send.py

# === 8. Scheduler Mingguan ===
echo "🔹 Menjadwalkan otomatis tiap 7 hari..."
python3 ~/automation_project/scripts/scheduler_weekly.py

# === 9. Logs & Queue Management ===
echo "🔹 Melihat log terbaru..."
tail -n 20 ~/automation_project/data/logs/*.log

echo "🔹 Cek email queue (kalau SMTP gagal)..."
ls ~/automation_project/data/email_queue

# === 10. Panduan Cepat ===
echo ""
echo "==========================================="
echo "✅ Semua script disimpan di:"
echo "   ~/automation_project/scripts/"
echo ""
echo "📊 Data & output tersimpan di:"
echo "   ~/automation_project/data/reports/"
echo ""
echo "🧠 Tips:"
echo " - Gunakan '--dry-run' sebelum kirim email"
echo " - Jalankan 'deactivate' untuk keluar dari env"
echo " - Backup token Gmail API di folder scripts/"
echo ""
echo "🐧 Automation CLI – By Akanra ✨"
echo "==========================================="
