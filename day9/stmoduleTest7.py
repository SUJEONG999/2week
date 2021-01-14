# =============== sys  ===============
import sys

print("버전 :", sys.version)
print("플랫폼 :", sys.platform)
if (sys.platform == "win32"):
    print(sys.getwindowsversion())
print("바이트 순서 :", sys.byteorder)
print("모듈 경로 :", sys.path)  # 현재 폴더가 가장 먼저 보임. 나머지는 파이썬 설치 경로
#sys.exit(0)

# =============== sysarg  ===============
import sys

print(sys.argv) # 소스명과 함께 출력

# =============== argcal  ===============
import calendar
import time
import sys

if (len(sys.argv) == 1):
    t = time.time()
    tm = time.localtime(t)
    calendar.prmonth(tm.tm_year, tm.tm_mon)  # 현재 년도와 월을 출력해서 calendar를 보여줌
elif (len(sys.argv) == 2): # Terminal 창에 2020 치기
    print(calendar.calendar(int(sys.argv[1])))
elif (len(sys.argv) == 3):  # Terminal 창에 2020 12 치기
    calendar.prmonth(int(sys.argv[1]), int(sys.argv[2]))
else:
    print("인수는 2개 이하여야 합니다.")