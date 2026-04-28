# while 조건문 (조건에 부합하지 않을 때까지 반복)
card_number = int(input("1~13까지 숫자를 입력하세요."))

expect = 1

# while card_number != expect:
#     print(f"음... {expect}도 아니군")
#     expect += 1

# print(f"내 생각에 너가 선택한 값은 {expect}야")

while True:
    if card_number == expect:
        break
    print(f"음... {expect}도 아니군")
    expect += 1
    
print(f"내 생각에 너가 선택한 값은 {expect}야")