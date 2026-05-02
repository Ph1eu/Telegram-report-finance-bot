import requests
from datetime import datetime

# ===== CONFIG =====
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def get_mock_data():
    return {
        "interbank_on": 3.8,
        "omo": 25000,
        "credit": 5.2,
        "margin": 180000
    }

def build_report(data):
    return f"""
📊 Weekly Monetary Report ({datetime.now().strftime('%Y-%m-%d')})

1. Interbank:
- O/N: {data['interbank_on']}%

2. OMO:
- Net injection: {data['omo']} tỷ

3. Credit:
- Growth YTD: {data['credit']}%

4. Margin:
- Estimate: {data['margin']} tỷ

"""

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })

if __name__ == "__main__":
    data = get_mock_data()
    report = build_report(data)
    send_telegram(report)
