import os
import requests

# 環境変数からアクセストークンを取得
ACCESS_TOKEN = os.getenv("THREADS_ACCESS_TOKEN")

def create_thread(title, content):
    url = "https://api.threads.com/v1/threads"  # Threads APIのエンドポイント
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",  # アクセストークンをヘッダーに設定
        "Content-Type": "application/json"
    }
    data = {
        "title": title,
        "content": content
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()
