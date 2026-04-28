log_data = ["LOGIN", "jeoneunji", "127.0.0.1"]

match log_data:
    case ["LOGIN", user, ip]:
        print(f"{user}가 {ip}에서 로그인했었네?")
    case ["LOGOUT", user]:
        print(f"{user}가 나갔네?")
    case _:
        print(f"대체 뭐지..? {log_data}")