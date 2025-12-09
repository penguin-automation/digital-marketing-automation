#!/bin/bash
# 🐧 Auto Update Script for Digital Marketing Automation CLI
# Made by Akanra 🐧 | Milestone 16+

PROJECT_DIR="$HOME/automation_project"
BRANCH="main"
COMMIT_MSG="${1:-✨ Update project automation system}"

echo "🐧 Moving to project folder..."
cd "$PROJECT_DIR" || { echo "❌ Folder not found!"; exit 1; }

echo "📦 Staging all changes..."
git add .

echo "📝 Committing with message: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

echo "🚀 Pushing to GitHub ($BRANCH)..."
git push -u origin "$BRANCH"

echo "✅ Done! Your updates are now live on GitHub 🌍"
echo "----------------------------------------------"
echo "🕒 $(date)"
echo "🐧 Keep coding, brokk!"
