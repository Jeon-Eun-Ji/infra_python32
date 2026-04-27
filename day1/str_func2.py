text = "문자열에 포함된 모든 문자의 개수(공백, 특수문자 포함)를 변환"

# 문자열 길이 반환
print(len(text)) # 길이 35

# 부분 문자열 개수 반환
print(text.count("문")) #3개

# find(), index()
print(text.find("포함")) # 5번째 없으면 -1
print(text.index("포함")) # 5번째 없으면 에러

python_path = "Users/Administrator/infra_python32/.venv/Scripts"
python_split_list = python_path.split("/")
print(python_split_list)
print("/".join(python_split_list))