def update_config(server_name, **kwargs):
    print(f"{server_name} 설정 변경 내역")
    for k, v in kwargs.items():
        print(f"{k} ----- {v}")
    
update_config("내 소중한 서버", os="Linux", port="22", status="Running", pw="1234")