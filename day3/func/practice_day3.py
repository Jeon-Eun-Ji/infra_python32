allowed_ips = ["1.1.1.1"]

def add_ip(new_ip):
    allowed_ips.append(new_ip)
    print(f"함수 내부 리스트: {allowed_ips}")

add_ip("2.2.2.2")
print(f"함수 외부 리스트: {allowed_ips}")