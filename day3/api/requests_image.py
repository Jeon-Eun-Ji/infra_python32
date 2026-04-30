import requests

try:
    code_input = int(input("상태 코드를 입력하세요"))

    if code_input < 200 or code_input > 599:
        raise ValueError("상태코드 아닙니다.")
    
    req_url = "https://http.cat/"+str(code_input)

    resp = requests.get(req_url)
    if resp.status_code == 200 and "image" in resp.headers.get("Content-Type"):
        with open(f"day3/api/cat{str(code_input)}.jpg", 'wb') as f:
            f.write(resp.content)
except Exception as e:
    print(e)