def hello_names(*names, count = 1):
    for name in names:
        print("Hello" * count, name)

# hello_names('손흥민', '이강인', '황희찬', 2)
# hello_names(2, '손흥민', '이강인', '황희찬')
# hello_names(count = 2, '손흥민', '이강인', '황희찬')
hello_names('손흥민', '이강인', '황희찬', count = 2)
# hello_names('손흥민', '이강인', '황희찬')