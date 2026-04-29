from pathlib import Path

# 경로 주의사항 : 터미널 경로 기준
# 디렉터리 존재 확인 - Path("경로").exists()
if not Path("day3/file_system/security_logs/daily").exists():
    # 디렉터리 생성 - Path("경로").mkdir(옵션)
    Path("day3/file_system/security_logs/daily").mkdir(parents=True)

# 파일 생성 - Path("경로").touch()
Path("day3/file_system/security_logs/daily/log.txt").touch()

# 파일명 추출
file_name = Path("day3/file_system/security_logs/daily/log.txt").name
print(file_name)
