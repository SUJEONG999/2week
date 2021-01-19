count=0
try:
    import re
    f = open("C:/jsj/PYTHONexam/day10/yesterday.txt", "r", encoding="UTF-8")
    for line in f:
        count += len(re.findall("Yesterday", line, re.IGNORECASE))
except FileNotFoundError:
    print("파일을 읽을 수 없어요")
else:
    print("Number of a Word 'Yesterday'",count)
    f.close()
finally:
    print("수행완료!!")

