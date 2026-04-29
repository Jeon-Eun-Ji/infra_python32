def setup_firewall(ip, port, action)
    print(f"{ip}:{port} 접속 후 {action}")

config = ["127.0.0.1", 80, "BLOCK"]

setup_firewall(*config)