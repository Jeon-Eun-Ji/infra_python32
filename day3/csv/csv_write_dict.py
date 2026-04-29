import csv

one_students = [
    {"name": "민병연", "city": "서울", "mbti": "INTJ"},
    {"name": "박건우", "city": "대구", "mbti": "ISTP"},
    {"name": "박민호", "city": "광주", "mbti": "ISTJ"},
    {"name": "박예은", "city": "인천", "mbti": "ESFJ"},
]

two_students = [
    {"name": "박진솔", "city": "경기", "mbti": "INTP"},
    {"name": "백세희", "city": "서울", "mbti": "ESTJ"},
    {"name": "백정민", "city": "부산", "mbti": "ISTP"},
    {"name": "양태규", "city": "광주 ", "mbti": "ENTP"},
]

three_students = [
    {"name": "서지우", "city": "서울"}, # INTJ
    {"name": "송보연", "city": "경기"}, # ISTJ
    {"name": "송석현", "city": "안양"}, # ESTJ
    {"name": "신지혜", "city": "인천"},
]

column_names = ["name", "city", "mbti"]

with open("day3\csv\student_analysis_report.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=column_names)
    writer.writeheader()
    writer.writerows(one_students)
    writer.writerows(two_students)
    writer.writerows(three_students)

print("끝")