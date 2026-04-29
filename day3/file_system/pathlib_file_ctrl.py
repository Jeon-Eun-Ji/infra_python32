from pathlib import Path
import shutil

text_content = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

source = Path("day3/file_system/security_logs/daily/log.txt")
if not source.exists():
    source.write_text(text_content, encoding="utf-8")

destination_dir = Path("day3/file_system/security_logs")
destination_path = destination_dir / "log1400.txt"
destination_path2 = destination_dir / "log1500.txt"

if source.exists():
    # 복사
    shutil.copy(str(source), str(destination_path))
    # source.copy(destination_path)
    # 이동
    shutil.move(str(source), str(destination_path2))
    # source.move(destination_path2)