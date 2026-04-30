import os
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_KEY")
DB_ID = os.getenv("DATABASE_ID")

if not NOTION_TOKEN or not DB_ID:
    raise ValueError(".env 값 없음 (┬┬﹏┬┬)")

url = f"https://api.notion.com/v1/databases/{DB_ID}"

# 헤더 설정
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

# 페이로드 작성
payload = {
    "title": [
        {
            "text": {
                "content": "제목 변경",
            },
        }
    ],
    "icon": {
        "type": "emoji",
        "emoji": "😎"
    },
}

try:
    # 요청 전송 (PATCH)
    response = requests.patch(url, headers=headers, json=payload, timeout=10)
    response.raise_for_status()

    print(response.json())

except requests.exceptions.HTTPError as e:
    # 401 TOKEN 값 문제 / 400, 404 경로 문제 or DB 접근 권한 문제
    print(f"노션 API 에러: {e}")
except Exception as e:
    print(f"알 수 없는 에러: {e}")