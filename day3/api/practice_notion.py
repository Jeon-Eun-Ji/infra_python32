import os
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_KEY")
DB_ID = os.getenv("DATABASE_ID")

if not NOTION_TOKEN or not DB_ID:
    raise ValueError(".env 값 없음 (┬┬﹏┬┬)")

# 헤더 설정
headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def get_all_pages():
    """상품 재고 DB의 모든 페이지 리스트 반환"""
    url = f"https://api.notion.com/v1/databases/{DB_ID}/query"
    response = requests.post(url, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json().get("results", [])

def delete_page(page_id):
    """특정 페이지를 아카이브(휴지통) 함"""
    url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = { "archived": True }
    response = requests.patch(url, headers=headers, json=payload, timeout=10)
    response.raise_for_status()
    return response.status_code == 200

try:
    pages = get_all_pages()
    if not pages:
        print("해당 DB에는 페이지가 없습니다.")
    else:
        print(f"[현재 상품 목록] (총 {len(pages)}개)")

        page_id_dict = {}

        for idx, p in enumerate(pages, 1):
            props = p.get("properties")

            # 이름 가져오기 (title 속성 값 가져오기)
            title_list = props.get("상품명", {}).get("title", [])
            title = title_list[0].get("plain_text") if title_list else None

            # 페이지 아이디 가져오기
            page_id = p.get("id", "id 없음")

            # 딕셔너리에 데이터 넣기
            page_id_dict[idx] = page_id

            # 출력
            print(f"{idx}번 --- {title} --- {page_id}")
        
        # 숫자 입력하세요
        choice = input("\n삭제할 페이지 번호를 입력하세요. (취소는 그냥 Enter): ")

        if choice.isdigit() and int(choice) in page_id_dict.keys():
            target_page_id = page_id_dict[int(choice)]
            if delete_page(target_page_id):
                print("휴지통 이동 완료 ☆*: .｡. o(≧▽≦)o .｡.:*☆")
            else:
                print("삭제 실패 (┬┬﹏┬┬)")
        else:
            print("취소되었거나, 잘못된 입력입니다. ಥ_ಥ")


except requests.exceptions.HTTPError as e:
    # 401 TOKEN 값 문제 / 400, 404 경로 문제 or DB 접근 권한 문제
    print(f"노션 API 에러: {e}")
except Exception as e:
    print(f"알 수 없는 에러: {e}")