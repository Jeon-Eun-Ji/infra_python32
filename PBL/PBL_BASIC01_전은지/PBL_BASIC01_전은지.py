# 1. 환경 설정 및 모듈 임포트
import os
import random
from dotenv import load_dotenv

load_dotenv() # .env 읽기
admin = os.getenv("ADMIN_NAME", "Guest")

# 2. 기초 데이터 선언
whitelist = ("192.168.1.10", "192.168.1.11") # 튜플은 변경 불가

server_assets = [
    {"name": "WEB-01", "ip": "192.168.1.10", "status": "Run"},
    {"name": "DB-01", "ip": "192.168.1.20", "status": "Stop"}
]

# 3. 입력 처리 (사용자 입력)
new_name = input("- 추가할 서버 이름: ")
new_ip = input("- 추가할 서버 IP: ")

server_assets.append({
    "name" : new_name,
    "ip" : new_ip,
    "status" : "Run",
    "cpu" : random.uniform(0, 100)
})

# 4. 데이터 수정 (첫 번째 서버 상태 Stop으로 변경)
server_assets[0]["status"] = "Stop"

# 5. 포맷팅 출력
print("- 총 3대의 서버의 보안 점검을 수행합니다.")
print("-" * 35)

s1 = server_assets[0]
s2 = server_assets[1]
s3 = server_assets[2]

print(f"[담당자: {admin}] {s1['name']} 서버({s1['status']}) 점검 수행")
print(f"- 화이트 리스트 대상 여부: {s1['ip'] in whitelist}")
print("-" * 35)

print(f"[담당자: {admin}] {s2['name']} 서버({s2['status']}) 점검 수행")
print(f"- 화이트 리스트 대상 여부: {s2['ip'] in whitelist}")
print("-" * 35)

print(f"[담당자: {admin}] {s3['name']} 서버({s3['status']}) 점검 수행")
print(f"- 화이트 리스트 대상 여부: {s3['ip'] in whitelist} / 현재 부하: {s3['cpu']:.1f}%")
print("-" * 35)