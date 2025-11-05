# 🐧 Digital Marketing Automation CLI

Automate your digital marketing tasks directly from Debian Terminal — built entirely using Python, Pandas, and the Gmail API.  
This project was created by **Akanra (Penguin Automation)** to bring professional marketing workflows into the Linux CLI ecosystem.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Debian%20CLI-lightgrey?logo=linux&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Automation](https://img.shields.io/badge/Automation-AI%20Insight-orange?logo=automation)
![GitHub last commit](https://img.shields.io/github/last-commit/penguin-automation/digital-marketing-automation)
![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)
![Made with ❤️ in Indonesia](https://img.shields.io/badge/Made%20with%20❤️-in%20Indonesia-red)

---

### ✨ Overview
A **Digital Marketing Automation CLI** built with Python and tested on Debian Linux 🐧.  
This project automates weekly marketing reports, generates visual engagement insights, and even sends emails using the Gmail API.

---

### ⚙️ Features
- 📊 **Engagement & AI Insight Analyzer**
- 🕓 **Auto Scheduler (Every 7 Days)**
- 📧 **Email Report Automation (via Gmail API)**
- 🧠 **AI-based Insight Generator**
- 📈 **Visual PDF & Portfolio Generator**
- 💾 **CLI Dashboard + Logging System**

---

### 🐧 Developer
**Author:** Akanra  
**GitHub:** [@penguin-automation](https://github.com/penguin-automation)  
**Built with:** ❤️, Debian, and a lot of ☕ + 🧠  

---

### 🌍 Languages
🇮🇩 **Indonesian (primary)**  
🇬🇧 **English (technical & docs)**  
🇪🇸 **Español (minor)**  

---

### 📜 License
This project is licensed under the MIT License — free to use, modify, and share!

---

## 🌍 Environment Setup / Configuración del Entorno

# 🇬🇧 English
Before running the automation system, make sure you set up your environment variables correctly.  
You can do this by creating a `.env` file based on the `.env.example` template provided in this repository.  

This file contains sensitive information like API keys or passwords — **never commit it** to GitHub.  

# Example `.env`
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

---

# 🇪🇦 Español

Antes de ejecutar el sistema de automatización, asegúrate de configurar correctamente tus variables de entorno.
Puedes hacerlo creando un archivo .env basado en el modelo .env.example incluido en este repositorio.

Este archivo contiene información sensible como claves API o contraseñas — nunca lo subas a GitHub.

# Ejemplo `.env`
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
