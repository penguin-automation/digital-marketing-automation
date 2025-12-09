#!/usr/bin/env python3
import requests
import os

def send_message(chat_id, text):
    with open("/etc/dma_bot_token", "r") as f:
        token = f.read().strip()
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    response = requests.post(url, json=payload)
    print(response.text)

if __name__ == "__main__":
    chat_id = input("Enter chat_id: ")
    send_message(chat_id, "🐧 Debian CLI Bot fresh start — online!")
