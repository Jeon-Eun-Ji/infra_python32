import random

server_names = [f"SVR-{i:02d}" for i in range(1, 16)]
raw_logs = [random.randint(1, 100) for _ in range(10)] + [0, "Error", None, 99, "Critical"]
random.shuffle(raw_logs)

print("--- 실시간 보안 점검 시스템 가동 ---")

# 반복 구조 설계
for log in raw_logs:
    #에러 가드 설치
    try:
        value = float(log)
        # 조건 우선순위 설정
        if value >= 99:
            print(f"[EMERGENCY] {value:.1f}% 감지! 해킹 의심으로 전체 점검 중단!")
            break
        elif value >= 90:
            print(f"-🔴 [CRITICAL] 사용률 {value:.1f}%: 즉시 서비스 차단 및 분리")
        elif value >= 70:
            print(f"-🟡 [WARNING] 사용률 {value:.1f}%: 관리자 호출 및 리소스 확장")
        elif value == 0:
            print(f"-⚪ [CHECK] 사용률 {int(value)}%: 장비 응답 없음 (전원 확인 요망)")
        else:
            print(f"-🟢 [NORMAL] 사용률 {value:.1f}%: 시스템 안정")

    except (ValueError, TypeError):
        print(f"-❌ [DATA ERROR] 읽을 수 없는 로그 형식입니다. (입력값: {log})")
        continue

    finally:
        print("-" * 15 + "점검 완료" + "-" * 15)
