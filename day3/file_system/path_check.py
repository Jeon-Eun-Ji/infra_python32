import os
from pathlib import Path

# os 모듈에서 사용되는 방식 : 문자열 덧셈 또는 join 함수
os_path = os.path.join("logs", "2026", "report.txt")
print(f"os 모듈에서 사용되는 경로는 {os_path}와 같은 모양이며, 타입은 {type(os_path)}")

# pathlib 모듈에서 사용되는 방식 : / 기호로 직관적인 연결이 가능
pathlib_path = Path("logs") / "2026" / "report.txt"
print(f"os 모듈에서 사용되는 경로는 {pathlib_path}와 같은 모양이며, 타입은 {type(pathlib_path)}")