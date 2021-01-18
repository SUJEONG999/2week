# =============== filecopy  ===============
import shutil
import os

if os.path.exists("live2.txt") :
   print("파일이 존재합니다.")
else :
   print("파일이 존재하지 않습니다.")

print("[ 파일 복사 ]")
shutil.copy("live.txt", "live2.txt")   # live.txt를 copy해서 live2.txt를 만들겠다.
if os.path.exists("live2.txt") :
   print("파일이 존재합니다.")
else :
   print("파일이 존재하지 않습니다.")


