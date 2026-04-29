import glob

py_file_os = glob.glob("day1/*.py")

print(f"day1 폴더의 파이썬 파일 개수 {len(py_file_os)}")

print("파이썬 파일 목록")
for f in py_file_os:
    print(f)