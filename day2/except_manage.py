
try:
    number = int(input("숫자를 입력하세요."))
    result = 100 / number
    print(result)
except ZeroDivisionError:
    print("0은 쓰지마 그건 나눌 수 없어")
except Exception as e:
    print(f"사고다 사고 사고 내용은 {e}")

print("또 다른 중요작업을 시작합니다.")
