# 기본 정보 설정 (튜플)
db_config = ("127.0.0.1", "admin", 1234)

# 수정 시도
#db_config[0] = "192.0.8.15"

# 출력
print(db_config[0])

# 요소가 하나 뿐인 튜플에는 ,를 찍어서 표시하자
single_tuple = (1,)
print(single_tuple)

#
def test(a, b):
    return a + b

print(test(1,2))
