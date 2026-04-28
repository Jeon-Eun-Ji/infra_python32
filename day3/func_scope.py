server_status = "정상"

def check_system():
    # server_status = "위험" # 있으면 내부에 있는 변수가 출력되나, 없으면 외부에 있는 변수가 나온다.
    print(f"함수 내부 - {server_status}")

check_system()
print(f"함수 외부 - {server_status}")