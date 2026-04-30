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

    a = response.text
    with open('day3/api/data.json', 'w', encoding="utf-8") as f:
        f.write(a)
    data = response.json()
    page_list = data.get("results", [])

    for page in page_list:
        props = page.get("properties")

        # 이름 가져오기 (title 속성 값 가져오기)
        title_list = props.get("상품명", {}).get("title", [])
        title = title_list[0].get("plain_text") if title_list else None

        # 수량
        qty = props.get("재고 수량", {}).get("number") or 0

        # 금액
        price = props.get("금액", {}).get("number") or 0

        # 총 금액
        total_price = props.get("총 금액", {}).get("formula", {}).get("number", 0)

        print(f"상품명: {title} | 수량: {qty} | 금액: {price:,} | 총 금액: {total_price:,}")

except requests.exceptions.HTTPError as e:
    # 401 TOKEN 값 문제 / 400, 404 경로 문제 or DB 접근 권한 문제
    print(f"노션 API 에러: {e}")
except Exception as e:
    print(f"알 수 없는 에러: {e}")