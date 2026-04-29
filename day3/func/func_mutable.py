ip_list = ["1.1.1.1"]

def append(new_ip):
    new_ip_list = [new_ip]
    return ip_list + new_ip_list

ip_list2 = append("2.2.2.2")
print(ip_list2)
print(ip_list)