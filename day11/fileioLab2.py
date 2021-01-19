import time

now = time.localtime()
try:
    fr = open("C:/jsj/PYTHONexam/day10/sample.txt", "rt", encoding="UTF-8")
    file_name = f"sample_{now.tm_year}_{now.tm_mon:02d}_{now.tm_mday:02d}.txt"
    fa = open(file_name, "at", encoding="UTF-8")

    for line in fr:
        fa.write(line)

    fr.close()
    fa.close()

except FileNotFoundError as e:
    print(e)
print("저장이 완료되었습니다.")