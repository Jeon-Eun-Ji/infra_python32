from pathlib import Path

py_file_pathlib = Path("day2").glob("*.py")

for f in py_file_pathlib:
    print(f"파일명: {f.name}, 파일크기: {f.stat().st_size}")