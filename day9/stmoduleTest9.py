import os
if not os.path.isdir("c:/Temp/log"): # 존재하는가?
    os.mkdir("c:/Temp/log") # temp 라는 directory에 가서 log 폴더를 만들어줘.
    print("c:/Temp/log 폴더 생성")
else : # True 이면
    print("c:/Temp/log 폴더는 이미 존재!!")