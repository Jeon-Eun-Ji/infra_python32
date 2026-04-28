inventory = [
    {"name" : "WEB1", "risk" : 95},
    {"name" : "DB2", "risk" : 40},
    {"name" : "DB3", "risk" : 50},
    {"name" : "WEB2", "risk" : 10},
    {"name" : "WEB3", "risk" : 75},
    {"name" : "DB4", "risk" : 83},

]

def filter_high_risk(list):
    """딕셔너리를 (keys[name, risk]요소로 하는 리스트를 받아, risk가 높은 서버의 name들을 리스트로 반환"""
    result = [dict["name"] for dict in list if dict["risk"] > 80]

    def result_func():
        print(result)
    return result_func

result = filter_high_risk(inventory)
result()