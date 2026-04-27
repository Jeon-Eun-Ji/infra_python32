import os
import dotenv

# 1 .env 내용을 환경변수로 로드
dotenv.load_dotenv()

# 2. os 모듈을 통해 값 가져오기
password = os.getenv("PASSWORD")

# 3. 값 확인
print(password)