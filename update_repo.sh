#!/bin/bash
# 🐧 Automation Repo Updater Script
# Simplify commit + push workflow for penguin-automation

REPO_PATH="$HOME/automation_project"
COMMIT_MSG="$1"

if [ -z "$COMMIT_MSG" ]; then
  echo "⚠️  Usage: ./update_repo.sh \"Your commit message\""
  exit 1
fi

echo "🐧 Moving to project folder..."
cd "$REPO_PATH" || exit

echo "📦 Staging changes..."
git add .

echo "📝 Committing with message: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

echo "🚀 Pushing to GitHub (origin/main)..."
git push origin main

echo "✅ Done! Your updates are now live on GitHub 🌍"
