#!/usr/bin/env python3
import os
import subprocess
from loguru import logger

# Lokasi file token GitHub (aman & permission 600)
TOKEN_PATH = os.path.expanduser("~/.github_token")
REPO_URL = "https://github.com/penguin-automation/digital-marketing-automation.git"

def load_token():
    with open(TOKEN_PATH, "r") as f:
        return f.read().strip()

def push_to_github(commit_message):
    token = load_token()
    repo_url = REPO_URL.replace("https://", f"https://{token}@")

    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", commit_message],
        ["git", "push", repo_url, "main"]
    ]

    for cmd in commands:
        logger.info(f"Running: {' '.join(cmd)}")
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed: {e}")
            exit(1)

    logger.success("✅ Successfully pushed changes to GitHub!")

if __name__ == "__main__":
    commit_msg = input("Enter commit message: ").strip()
    push_to_github(commit_msg)
