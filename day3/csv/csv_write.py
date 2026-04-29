import csv

report_data = [
    ["호스트네임", "아이피주소", "상태", "최근 체크"],
    ["WEB-01", "192.168.1.10", "Safe", "2026-04-03"],
    ["DB-01", "192.168.1.20", "Vulnerable", "2026-04-03"],
    ["APP-01", "192.168.1.30", "Safe", "2026-04-03"]
]

with open("day3/csv/daily_security_report.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerows(report_data)

print("끝")