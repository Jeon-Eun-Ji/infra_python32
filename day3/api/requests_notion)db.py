import os
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_KEY")
DB_ID = os.getenv("DATABASE_ID")

if not NOTION_TOKEN or not DB_ID:
    raise ValueError(".env 값 없음 (┬┬﹏┬┬)")

url = f"https://api.notion.com/v1/databases/{DB_ID}/query"

# 헤더 설정
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

try:
    # 요청 전송 (POST)
    response = requests.post(url, headers=headers, timeout=10)
    response.raise_for_status()

    data = response.json()
    print(data)

except Exception as e:
    print(e)