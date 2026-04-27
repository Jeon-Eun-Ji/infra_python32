message="위험-사용자인증실패-2026-04-27"

msg_list = message.split("-")
risky_level = msg_list[0]
real_msg = msg_list[1]
date_list = msg_list[2:]

print(risky_level, real_msg, date_list)

names = "    가, 나, 다, 라, 마, \n바, 사   \n\n\n\n "
print(names)
print(names.strip())

print(names.strip().replace(" ","").replace("\n",",").replace("," , "\n"))