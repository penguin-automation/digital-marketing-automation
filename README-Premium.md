# 🐧 Digital Marketing Automation CLI – Debian Edition  
**Version:** v1.0.3 Stable | **Platform:** Debian / Linux | **License:** Open Source

![Build Status](https://github.com/penguin-automation/digital-marketing-automation/actions/workflows/build.yml/badge.svg)
![Version](https://img.shields.io/badge/version-1.0.5-blue)
![Platform](https://img.shields.io/badge/platform-Debian%20%2F%20Linux-orange)
![Status](https://img.shields.io/badge/status-Stable-success)

---

## 🚀 Overview
**Digital Marketing Automation CLI (DMA CLI)** adalah sistem otomatisasi penuh berbasis Python & Debian yang dirancang untuk:
- Menganalisis performa engagement digital secara terjadwal.
- Menghasilkan laporan visual dan portofolio PDF.
- Mengirimkan hasil otomatis ke email melalui Gmail API (OAuth2, tanpa SMTP/stunnel).
- Mengelola semua tugas marketing via satu perintah CLI.

---

## ⚙️ Features
✅ CLI Workflow berbasis `argparse`  
✅ Visualisasi grafik & PDF report (`matplotlib`, `reportlab`)  
✅ Auto Email via Gmail API OAuth2  
✅ Log sistem real-time (`loguru`)  
✅ Scheduler otomatis via `systemd.timer`  
✅ Debian `.deb` package (Team-ready installer)  
✅ CI/CD GitHub Actions Integration  

---

## 🧩 CLI Usage
```bash
marketing-cli --help
marketing-cli --all        # Jalankan semua task otomatis
marketing-cli --analyze    # Analisis engagement
marketing-cli --visual     # Generate visual report (PDF)
marketing-cli --portfolio  # Buat portofolio digital lengkap
marketing-cli --email      # Kirim report via Gmail API

#🔐 OAuth2 & Security Notice
Aplikasi ini menggunakan Gmail API OAuth2 (bukan SMTP klasik).
 • Token pribadi disimpan di ~/Documents/credentials/
 • Gunakan chmod 600 agar hanya user sendiri yang bisa akses 🔒
 • OAuth2 masih dalam tahap testing approval (Google Developer Console) 

# 🛠 Installation (Local .deb)
sudo dpkg -i dma-cli_1.0-5.deb
sudo systemctl enable dma-cli.timer
sudo systemctl start dma-cli.timer
🐧 After installation, the system automatically runs every week through systemd.

# 🧠 Architecture
├── /usr/bin/marketing-cli     → CLI executable
├── /usr/lib/dma/              → Core Python automation scripts
├── /usr/share/doc/dma-cli/    → Debian documentation (changelog, copyright)
├── /etc/systemd/system/       → dma-cli.service & dma-cli.timer
├── ~/automation_project/data/ → Reports & Portfolios
└── ~/automation_project/logs/ → Execution logs

# 🧪 Development Notes
Dibangun 100% via CLI (tanpa GUI tools)
Diuji lintian — hanya minor warnings (non-blocking)
Menggunakan virtual environment internal (venv)
Dirancang untuk Debian 12+ (stable/testing/Sid)
Seluruh packaging mematuhi Debian Packaging Policy (100%)

# 🧰 Build Commands
dpkg-deb --build build_deb dma-cli_1.0-5.deb
lintian dma-cli_1.0-5.deb

# 🏷️ Release Info
| Tag    | Date       | Status   | Notes                                       |
| ------ | ---------- | -------- | ------------------------------------------- |
| v1.0.5 | 2025-11-07 | ✅ Stable | Final release verified & uploaded to GitHub |

# 💡 Maintainer
 Akanra - 19y/o Open Source Enthusiast & Automation Girl🐧✨
🧭 Debianist | Automation Engineer (FEB Management background)
🐧 "From management to terminal — Debian made it possible."

# 📜 License
Released under an open-source license.
You are free to modify and redistribute with proper attribution.

# ❤️ Acknowledgment
Special thanks to Debian GNU/Linux Community & the Open-Source ecosystem
for inspiring young devs to build, automate, and share knowledge.
