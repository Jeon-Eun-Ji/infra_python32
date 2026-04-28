# 여러 개의 인자 *args / 출력 횟수 = 1

def print_numbers(*args, count = 1):
    for _ in range(count):
        print(args)


print_numbers(3, 3, 3, count = 3)