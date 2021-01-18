f = open("live.txt", "rt", encoding="UTF-8")
while True:
    text = f.read(10) # 10문자씩 읽기
    if len(text) == 0: break
    print(text, end = '$')
f.close()
print("\n"+"-"*20)

f = open("live.txt", "rt", encoding="UTF-8")
text = ""
line = 1
while True:
    row = f.readline() # 한 행씩 읽기
    if not row: break
    text += str(line) + " : " + row
    line += 1
f.close()
print(text)
print("\n"+"-"*20)

f = open("live.txt", "rt", encoding="UTF-8")
rows = f.readlines()  # 모든 행을 한꺼번에 읽어서 리스트로 리턴
for row in rows:
    print(row, end = '')
f.close()

print("\n"+"-"*20)
f = open("live.txt", "rt", encoding="UTF-8")  # 중요
for line in f:        # _io.TextIOWrapper 객체도 리터러블함
    print(line, end = '') # 행단위로 읽어서 반복문에 쓸수 있다.
f.close()