# 계산기

# 더하기 함수, 빼기 함수, 곱하기 함수, 나누기 함수
def sum(a, b):
    return a + b

def substact(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("0으로는 나눌 수 없습니다.")
        return None
    return a / b

def calculator():
    input_a = int(input("숫자 입력: "))
    input_b = int(input("숫자 입력: "))
    input_action = input("행동 입력(더하기, 빼기, 곱하기, 나누기): ")
    if input_action == "더하기":
        real_action = sum
    elif input_action == "빼기":
        real_action = substact
    elif input_action == "곱하기":
        real_action = multiply
    elif input_action == "나누기":
        real_action = divide
    else:
        real_action = None
    return [input_a, input_b, real_action]

def real_calc(input_a, input_b, real_action):
    return real_action(input_a, input_b)

[a, b, c] = calculator()
print(real_calc(a, b, c))