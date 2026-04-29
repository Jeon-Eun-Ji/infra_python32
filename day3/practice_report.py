raw_data = [22, 80, 443, 8080, 21] 

# filter와 lambda를 사용해 100번 미만의 잘 알려진 포트만 골라주세요.
port = filter(lambda x: x < 100, raw_data)

# map과 lambda를 사용해 골라낸 포트 뒤에 ":OPEN"이라는 문구를 붙여주세요.
opened_port = map(lambda x: f"{x}:OPEN", port)

# 출력 예시
# ['22:OPEN', '80:OPEN', '21:OPEN']
result = list(opened_port)
print(result)