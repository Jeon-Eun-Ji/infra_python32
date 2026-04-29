def send_alert(server_name, status):
    """DocString: 함수 가이드 [서버 메시지 출력]"""
    print(f"🚨[경보] 대상 장비는 {server_name}")
    print(f"🚨[상태] 현재 상황은 {status}")
    print("-"*20)

send_alert("DB-01", "DB 용량 초과")