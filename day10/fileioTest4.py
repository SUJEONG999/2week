f = open("live.txt", "rt", encoding="UTF-8", errors='ignore')
print("[seek기능 처리가능]" if f.seekable() else "[seek기능 처리불가]" )
f.seek(12,0) # 한글은 3바이트, 원하는 바이트만큼 건너 뛰어서 읽겠다는 의미
text = f.read()
f.close()
print(text)

# =============== append  ===============
f = open("live.txt", "at", encoding="UTF-8")
f.write("\n\n[추가]푸쉬킨 형님의 말씀이었습니다.")
f.close()

# =============== withas  ===============
with open("live.txt", "rt", encoding="UTF-8") as f: # 객체 담을 변수 f
   text = f.read()  # with 블록 수행되면 자동으로 닫힘.
print(text)  # 따로 close 처리 안해도 된다.

help(f.seek)