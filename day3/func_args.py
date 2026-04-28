def check_servers(*args):
    print(type(args))
    print(f"총 길이 {len(args)}")
    for s in args:
        print(s)


check_servers("서버1", "서버2", "서버3", "서버4")