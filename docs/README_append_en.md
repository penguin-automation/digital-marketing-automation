# 🚀 Full Automation: End-to-End Marketing CLI Workflow

This update introduces a unified command-line automation system for digital marketing tasks — analyze, visualize, generate, and deliver reports all in one go.  
From data insight to email delivery, everything runs seamlessly in one command.

## 🧩 Features Added (Milestone 16)
- **CLI Unified Workflow:** Run all major marketing tasks with `--all`.
- **Automated Gmail API Integration:** Secure email sending via OAuth2 (no SMTP or app passwords).
- **Dynamic Portfolio & Report Generation:** Automatically builds visual and textual reports from engagement data.
- **Modular Design:** Each component (analyze, visualize, report, email) can still run independently.
- **Logging System:** All activity stored in `logs/system_run.log`.

## 💻 Quick Demo

```bash
python3 marketing_cli.py --all

## Output Example
✅ Analyze complete  
✅ Visual report generated  
✅ Portfolio generated  
✅ Email sent successfully
🎯 All processes finished!

## Why This Matters
This project is designed for digital marketers, freelancers, and automation engineers who want to 
handle campaign data from start to finish in one terminal flow — completely transparent, reproducible, and offline-capable.

🇮🇩 Made proudly in Indonesia — by Akanra 🐧
