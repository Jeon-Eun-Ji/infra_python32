beverage_dict = {
    1 : {"name" : "콜라", "price": 500},
    2 : {"name" : "사이다", "price": 600},
    3 : {"name" : "환타", "price": 700},
    4 : {"name" : "밀키스", "price": 800},
    5 : {"name" : "포카리스웨트", "price": 900},
}

money = 0

# def 로 분할
def show_menu():
    print("="*60)
    for k, v in beverage_dict.items():
        print(f"{k} : {v["name"]}")
    print("="*60)

def get_money(money):
    try:
        input_money = int(input("금액을 넣으세요"))
    except:
        raise ValueError("숫자만 입력 가능합니다.")
    return money + input_money

def input_beverage():
    try:
        beverage_num = int(input("마시고 싶은 음료를 선택하세요! 종료는 0번"))
    except:
        raise ValueError("숫자만 입력 가능합니다.")
    # 입력 예외 처리
    if not beverage_num:
        return None
    elif beverage_num < 1 or beverage_num > 5:
        raise ValueError("요구하는 형식의 값이 아닙니다.")
    return beverage_dict[beverage_num]

def give_change(money):
    # 잔돈이 0원이면, 잔돈 줄필요 있나? 없죠?
    # 잔돈이 -면.. 애초에 음료를 주면 안되요!
    # 잔돈이 +면... 잔돈 드려야죠...
    print(f"땡그랑! 잔돈 {money}원 입니다.")

def serve_beverage(money, beverage):
    if money >= beverage["price"]: 
        print(f"{beverage["name"]}이/가 나왔습니다.")
        money -= beverage["price"]
    else:
        print("금액이 부족합니다.")
    return money

while True:
    # 사용자로부터 숫자를 입력받아 금액을 추가한다.
    try:
        money = get_money(money)
        print(f"입금 금액: {money}")
    except Exception as e:
        print(e)
        continue

    # 단순 메뉴 출력
    show_menu()

    while True:
        # 음료 입력받기
        try:
            selected_beverage = input_beverage()
            break
        except Exception as e:
            print(e)
            continue
        
    if selected_beverage == None:
        break

    # 음료 제공
    money = serve_beverage(money, selected_beverage)

    # 잔돈 계산
    give_change(money)