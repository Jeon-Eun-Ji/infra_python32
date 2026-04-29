import re

text = """203.0.113.211 - - [01/May/2026:00:27:02 +0900] "GET /dashboard HTTP/1.1" 200 10417 "https://example.internal/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
192.0.2.121 - - [01/May/2026:00:29:40 +0900] "GET /api/metrics HTTP/1.1" 403 153 "-" "curl/8.6.0"
10.12.4.19 - - [01/May/2026:00:30:12 +0900] "GET /health HTTP/1.1" 200 17 "-" "curl/8.6.0"
203.0.113.56 - - [01/May/2026:00:33:21 +0900] "GET /products HTTP/1.1" 200 7312 "https://example.internal/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"""

ip_addr_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", text)

print(ip_addr_list)
print(f"접속된 아이피 주소 정리 - {set(ip_addr_list)}")