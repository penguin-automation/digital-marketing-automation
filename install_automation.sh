#!/bin/bash
echo "🐧 Installing Digital Marketing Automation CLI..."
sleep 1

# 1. Cek virtual environment
if [ ! -d "$HOME/venv/automation" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv ~/venv/automation
fi

# 2. Activate environment
source ~/venv/automation/bin/activate

# 3. Install dependencies
echo "⚙️ Installing Python dependencies..."
pip install --upgrade pip
pip install loguru pandas matplotlib reportlab google-auth google-auth-oauthlib google-auth-httplib2

# 4. Set execute permissions
chmod +x ~/automation_project/scripts/*.py

# 5. Done
echo "✅ Installation complete!"
echo "To run the demo, use:"
echo "👉 python3 ~/automation_project/scripts/demo_run.py"
