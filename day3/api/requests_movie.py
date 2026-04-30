# /boxoffice/searchDailyBoxOfficeList.json?key={}&targetDt={}

import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

if not API_KEY or not BASE_URL:
    raise ValueError(".env 값 없음 (ㅠ-ㅠ)")

parameters = {"key" : API_KEY, "targetDt":"20260401"}

try :
    response = requests.get(f"{BASE_URL}/boxoffice/searchDailyBoxOfficeList.json", params = parameters, timeout=5)
    response.raise_for_status()
    # print(response.json())
    # 상태코드 확인
    print(f"상태코드: {response.status_code}")
    # 실제 최종 주소 확인
    print(f"최종 요청  URL: {response.url}")
    # 응답 헤더 중 Content-Type 확인
    print(f"데이터 형식 : {response.headers.get("Content-Type", "타입 없음")}")
    # 인코딩 확인 
    print(f"현재 인코딩 : {response.encoding}")

    # 결과
    data_result = response.json()
    title = data_result.get("boxOfficeResult").get("boxofficeType")
    daily_box_office_list = data_result.get("boxOfficeResult").get("dailyBoxOfficeList")
    
    print("="*60)
    print(title)
    print("="*60)
    for movie in daily_box_office_list:
        print(f"{movie['rank']}위: {movie['movieNm']} --- (관객수: {movie['audiAcc']}명)")
    # 텍스트로 결과 확인
    # print(f"결과 : {response.text[:50]}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP 에러 (상태코드 확인): {e}")
except requests.exceptions.RequestException as e:
    print(f"네트워크 통신 에러: {e}")
except Exception as e:
    print(f"알 수 없는 에러 : {e}")