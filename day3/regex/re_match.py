import re

log_entry = "[ERROR] 인증없는 접근 시도 (IP: 192.168.0.1)"

pattern = r"\[ERROR\]"

m = re.match(pattern, log_entry)

if m:
    print(f"보안 위협 탐지: {m.group()} 유형의 로그입니다.")
else:
    print("일치하는 로그가 없습니다.")