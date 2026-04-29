import json

# 문자열을 가져와서 dictionary로 변환

# raw_json_str는 json 형태를 갖고 있지만... 그냥 문자열인 상태
raw_json_str = '[{"name": "안다솜", "city": "경기", "mbti": "ISTP", "sibling": 1, "pbl": false}, {"name": "양태규", "city": "광주", "mbti": "ENTP", "sibling": 0, "pbl": null}, {"name": "엄민욱", "city": "파주", "mbti": "ENFJ", "sibling": 2, "pbl": true}, {"name": "오승백", "city": "천안", "mbti": "ESFJ", "sibling": 2, "pbl": true}, {"name": "우유엘", "city": "수원", "mbti": "INTP", "sibling": 2, "pbl": false}]'
json_list = json.loads(raw_json_str)
for s in json_list:
    print(s["name"])

# students.json 파일을 가져와서 dictionary로 변환
with open("day3/json/students.json", "r", encoding="utf-8") as f:
    student_list = json.load(f)
    for s in json_list:
        print(s["name"])
