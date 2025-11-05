# 🐧 Digital Marketing Automation CLI

Automate your digital marketing tasks directly from Debian Terminal — built entirely using Python, Pandas, and the Gmail API.  
This project was created by **Akanra (Penguin Automation)** to bring professional marketing workflows into the Linux CLI ecosystem.

---

## 🌍 Environment Setup / Configuración del Entorno

### 🇬🇧 English
Before running the automation system, make sure you set up your environment variables correctly.  
You can do this by creating a `.env` file based on the `.env.example` template provided in this repository.  

This file contains sensitive information like API keys or passwords — **never commit it** to GitHub.  

#### Example `.env`
```bash
SENDER_EMAIL=example@gmail.com
APP_PASSWORD=abcd efgh ijkl mnop
GOOGLE_CLIENT_SECRET=path/to/client_secret.json
GOOGLE_TOKEN=path/to/token.json
REPORT_DIR=~/automation_project/data/reports
LOG_DIR=~/automation_project/logs

cp .env.example .env
nano .env
source ~/venv/automation/bin/activate
python3 scripts/auto_email_report.py --dry-run

### 🇪🇦 Español

Antes de ejecutar el sistema de automatización, asegúrate de configurar correctamente tus variables de entorno.
Puedes hacerlo creando un archivo .env basado en el modelo .env.example incluido en este repositorio.

Este archivo contiene información sensible como claves API o contraseñas — nunca lo subas a GitHub.

### Ejemplo .env
SENDER_EMAIL=example@gmail.com
APP_PASSWORD=abcd efgh ijkl mnop
GOOGLE_CLIENT_SECRET=path/to/client_secret.json
GOOGLE_TOKEN=path/to/token.json
REPORT_DIR=~/automation_project/data/reports
LOG_DIR=~/automation_project/logs

### Configuración Rápida
cp .env.example .env
nano .env
source ~/venv/automation/bin/activate
python3 scripts/auto_email_report.py --dry-run


🚀 Features

✅ CLI Dashboard for marketing stats
✅ Automated Email Reporting (Gmail API)
✅ AI-based Engagement Analysis
✅ Weekly Scheduler
✅ Local Insight Engine (No API needed)
✅ Secure logging system
✅ PDF Report Generation


🐧 Author

Akanra (Penguin Automation)
🗺️ From Maumere → Based in Malang
💻 Freelance Debian Automation Developer
🌐 Project GitHub: penguin-automation/digital-marketing-automation 
