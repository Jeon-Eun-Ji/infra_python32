from pathlib import Path
import shutil

# log1500.txt -> log1408.txt

source = Path("day3/file_system/security_logs/log1500.txt")
dest =  Path("day3/file_system/security_logs/log1408.txt")

if source.exists():
    # shutil.move(str(source), str(dest))
    source.rename(dest)