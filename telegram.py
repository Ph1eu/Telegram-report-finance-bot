import requests
import os

def send(msg):
    url = f"https://api.telegram.org/bot{os.getenv('BOT_TOKEN')}/sendMessage"

    requests.post(url, data={
        "chat_id": os.getenv("CHAT_ID"),
        "text": msg
    })