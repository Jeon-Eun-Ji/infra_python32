import re

text = "내 전번은 010-1234-5678이야."
pattern = r"(\d{3})-(\d{4})-(\d{4})"

m = re.search(pattern, text)

if m:
    print(m.group()) # 전체에 대한 매칭
    print(m.group(0)) # 전체에 대한 매칭
    print(m.group(1)) # 1번 그룹에 대한 매칭
    print(m.group(2)) # 2번 그룹에 대한 매칭
    print(m.group(3)) # 3번 그룹에 대한 매칭

text = "2026-04-30"
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
m = re.search(pattern, text)

if m:
    print(m.group("year")) # 1번 그룹에 대한 매칭
    print(m.group("month")) # 2번 그룹에 대한 매칭
    print(m.group("day")) # 3번 그룹에 대한 매칭

print(re.sub(pattern, r"\1년 \2월 \3일", text))