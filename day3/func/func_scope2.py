policy = "차단"

def change_policy():
    print(policy)
    policy = "허용"
    print(f"함수 내 정책: {policy}")

change_policy()
print(f"최종 정책: {policy}")