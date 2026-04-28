def scan_network(ip, port=80):
    print(f"ip 주소 : {ip}의 {port} 포트를 스캔합니다.")

scan_network("127.0.0.1")
scan_network("127.0.0.1", 443)