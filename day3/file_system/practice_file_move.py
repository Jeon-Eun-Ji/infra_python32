from pathlib import Path

# 다운로드 폴더 경로
downloads_path = Path.home() / "Downloads"

# 다운로드 폴더 내 파일 목록 출력
print("-------------------- 다운로드 파일 목록 --------------------")
file_list = [f for f in downloads_path.iterdir() if f.is_file()]
for idx, file in enumerate(file_list): 
    print(f"{idx+1:02d} : {file.name}")

# 사용자의 선택
choice = int(input("파일 번호를 선택하세요")) -1
selected_file = file_list[choice]

# 목적지 경로
destination_path = Path(".")

# 파일 복사
selected_file.copy(destination_path / selected_file.name)

print("복사 완료")