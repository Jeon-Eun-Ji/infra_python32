logs = ["Login Success", "Attack Detected", "Logout"]

attack_msg_list = [f"{i}---{msg}" for i, msg in enumerate(logs, start=1) if "Attack" in msg]
# for i, msg in enumerate(logs, start=1):
#     if "Attack" in msg:
#         attack_msg_list.append(f"{i}---{msg}")

print(attack_msg_list)