import requests

# [GET] 정보 요청
response = requests.get("https://api.ipify.org?format=json")

if response.status_code == 200:
    print(response.json()["ip"])
    print(response.text)
else:
    print(response.status_code)