#!/usr/bin/env python3
import os
import time
from loguru import logger

logger.info("🐧 Welcome to Digital Marketing Automation CLI Demo!")
time.sleep(1)

# Step 1: Run engagement analysis
logger.info("📊 Running engagement analysis...")
os.system("python3 ~/automation_project/dma/analyze_engagement.py")
time.sleep(1)

# Step 2: Generate visual report
logger.info("🎨 Generating visual PDF report...")
os.system("python3 ~/automation_project/generate_visual_report.py")
time.sleep(1)

# Step 3: Run CLI dashboard
logger.info("📈 Displaying mini CLI dashboard (press Ctrl+C to exit)...")
time.sleep(1)
os.system("python3 ~/automation_project/dma/cli_dashboard.py")

logger.success("✅ Demo completed successfully!")
