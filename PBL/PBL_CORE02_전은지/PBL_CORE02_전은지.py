from pathlib import Path
import csv
import json

# 실무형 로그 데이터 생성 (날짜 | 시간 | Src_IP | Dst_IP | Port | Action)
log_data = """2026-04-06 | 10:01:22 | 192.168.1.10 | 10.0.0.1 | 443 | ALLOW
2026-04-06 | 10:05:45 | 211.23.45.10 | 10.0.0.1 | 22 | BLOCK
2026-04-06 | 10:12:10 | 192.168.1.20 | 10.0.0.2 | 80 | ALLOW
2026-04-06 | 10:15:33 | 10.0.0.55 | 10.0.0.1 | 3389 | BLOCK
2026-04-06 | 10:20:01 | 127.0.0.1 | 127.0.0.1 | 8080 | ALLOW"""

Path("PBL/PBL_CORE02_전은지/firewall_access.log").write_text(log_data, encoding="utf-8")
print("✅ 실무형 방화벽 로그 파일(firewall_access.log) 생성 완료!")

# 함수 설계
def is_allowed(ip):
    whitelist = ("192.168.1.10", "192.168.1.20", "127.0.0.1")
    return ip in whitelist

# 로그 데이터 처리
lines = Path("PBL/PBL_CORE02_전은지/firewall_access.log").read_text(encoding="utf-8").splitlines()

ips = []

# 데이터 파싱 strip() -> 공백 제거
for line in lines:
    parts = [p.strip() for p in line.split("|")]
    if len(parts) >= 3:
        ips.append(parts[2]) # Scr_IP

# 고급 필터
unauthorized_ips = list(filter(lambda ip: not is_allowed(ip), ips))

# csv 저장
with open("PBL/PBL_CORE02_전은지/unauthorized_ips.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Detected_IP", "Risk_Level"])
    writer.writeheader()

    for ip in unauthorized_ips:
        writer.writerow({
            "Detected_IP": ip,
            "Risk_Level": "High"
        })

# JSON 저장 null 확인하기
json_data = {"unauthorized_ips": unauthorized_ips, "Status": None}
with open("PBL/PBL_CORE02_전은지/security_alert.json", "w", encoding="utf-8") as f:
    json.dump(json_data, f, indent=4)