import os

# 경로 주의사항 : 터미널 경로 기준
# 디렉터리 존재 확인 - os.path.exists("경로")
if not os.path.exists("day3/file_system/security_logs/daily"):
    # 디렉터리 생성 - os.makedirs("경로") : 줄줄이 생성
    os.makedirs("day3/file_system/security_logs/daily")

# 파일 생성
with open("day3/file_system/security_logs/daily/log.txt", "w") as f:
    f.write("test")

# 파일명 추출
file_name = os.path.basename("day3/file_system/security_logs/daily/log.txt")
print(file_name)