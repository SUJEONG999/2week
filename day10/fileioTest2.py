try:
    f = open("live.txt", "rt", encoding="UTF-8") # 읽어옴
    print(f, type(f))
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()

print("*"*20)
f = None
try:
    f = open("live.txt", "rt", encoding="utf8")  # UTF-8와 결과 동일함.
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    if f : # f에 객체가 대입된 상황인지 확인
        f.close()

