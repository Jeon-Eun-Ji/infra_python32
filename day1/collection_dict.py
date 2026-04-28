server_info = {
    "hostname": "WEB-SVR-01",
    "port": "80",
    "status": "Running",
    "ip_addr": "127.0.0.1",
    "os": "Ubuntu",
    "user_list": ["leeyun0528-cyber", "d0hiru", "Bul1etBear"]
}

# print(server_info["hostname"])
# print(server_info["port"])
# print(server_info["status"])
# print(server_info["ip_addr"])
# print(server_info["os"])
# print(server_info["user_list"])
# print(server_info["password_list"]) # 없는 키 -> 에러

server_info["port"] = 8080

print(server_info.get("hostname"))
print(server_info.get("port"))
print(server_info.get("status"))
print(server_info.get("ip_addr"))
print(server_info.get("os"))
print(server_info.get("user_list"))
print(server_info.get("password_list", "비밀~"))

# 딕셔너리 핵심 함수 (keys, values, items)
print(list(server_info.keys())[0])
print(list(server_info.values())[0])
print(list(server_info.items())[0])