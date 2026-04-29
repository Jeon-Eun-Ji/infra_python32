import json

students = [
    {"name": "안다솜", "city": "경기 ", "mbti": "ISTP", "sibling": 1, "pbl": False},
    {"name": "양태규", "city": "광주", "mbti": "ENTP", "sibling": None, "pbl": None},
    {"name": "엄민욱", "city": "파주", "mbti": "ENFJ", "sibling": 2, "pbl": True},
    {"name": "오승백", "city": "천안", "mbti": "ESFJ", "sibling": 2, "pbl": True},
    {"name": "우유엘", "city": "수원", "mbti": "INTP", "sibling": 2, "pbl": False},
]

# dictionary -> 문자열(str)
json_str = json.dumps(students, indent=4, ensure_ascii=False)
print(json_str)

# dictionary -> 파일 객체로 써준다.
with open("day3/json/students.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4, ensure_ascii=False)