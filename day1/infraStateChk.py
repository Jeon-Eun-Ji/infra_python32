import random

#관리자 이름 묻기
name = input ("관리자 이름을 입력하세요: ")

# 서버 ID 생성 (random 모듈 import)
random_id = random.randint (1, 50)
id_str = f"SVR-{random_id:02d}"

# CPU 사용률 생성
random_float_cpu = random.uniform (0.0, 100.0)
cpu_percent = f"{random_float_cpu:.1f}%"

random_log = random.randint(1000, 1000000)

print(f"[점검 보고서] 담당자: {name}/{id_str} {cpu_percent} / 누적 로그 수 : {random_log:,}")