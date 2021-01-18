# =============== listdir  ===============
import os

files = os.listdir("c:\\Temp") # temp 디렉토리에 있는 파일에 대한 정보를 list 객체로 리턴하시오.
print(type(files))
for f in files:
    print(f)

# =============== listdir2  ===============
import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = path + "\\" + f
        if os.path.isdir(fullpath):  # 디렉토리 이라면
            print("[" + fullpath + "]")  # 대괄호와 함께 출력
            dumpdir(fullpath)
        else: # 디렉토리 아니라면
            print("\t" + fullpath)  # 들여쓰기 되어서 경로 출력

dumpdir("c:\\jsj\\PYTHONexam") # / 로 주어도됨. 단 한개. / 혹은 \\
