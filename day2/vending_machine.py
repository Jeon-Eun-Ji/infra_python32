try:
    while True:
        money = int(input("돈을 넣어주세요"))
        beverage_dict = {
            1 : {"name" : "콜라", "price": 500},
            2 : {"name" : "사이다", "price": 600},
            3 : {"name" : "환타", "price": 700},
            4 : {"name" : "밀키스", "price": 800},
            5 : {"name" : "포카리스웨트", "price": 900},
        }
        print("="*60)
        print("마시고 싶은 음료를 선택하세요! 종료는 0번")
        for k, v in beverage_dict.items():
            print(f"{k} : {v["name"]}")
        print("="*60)
        beverage_num = int(input("마시고 싶은 음료번호를 입력하세요"))
        
        if not beverage_num:
            break

        beverage_name = beverage_dict[beverage_num]["name"]
        beverage_price = beverage_dict[beverage_num]["price"]

        if beverage_price == money:
            print(f"덜컹! {beverage_name}이/가 나왔습니다.")
        elif beverage_price < money:
            print(f"덜컹! {beverage_name}이/가 나왔습니다.")
            change = money - beverage_price
            print(f"땡그랑! 잔돈 {change}원 입니다.")
        else:
            print("입금하신 금액이 부족합니다.")
            print(f"땡그랑! {money}원이 반환됩니다.")
except Exception as e:
    print(e)