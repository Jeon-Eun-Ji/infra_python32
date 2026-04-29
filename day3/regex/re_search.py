import re

log = [
    "192.168.0.1 - [05/Apr/2026] GET /etc/passwd 403",
    "192.168.0.10 - [05/Apr/2026] GET /index.html 200",
    "192.168.0.1 - [05/Apr/2026] GET /index.html 200",
    "192.168.0.20 - [05/Apr/2026] GET /index.html 200"
]

ip_set = set()

# 접속 로그에서 아이피 주소 가져오기
for i in log: 
    match = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", i)
    if match:
        ip_set.add(match.group())

print(ip_set)