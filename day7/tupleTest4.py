import time
def gettime():
    now = time.localtime()
    print(now, type(now))
    return now.tm_hour, now.tm_min  # 자동으로 패킹이 일어나서 튜플로 묶어줌

result = gettime()
print("지금은 %d시 %d분입니다" % (result[0], result[1]))

hour, minute = gettime()  # 언패킹 일어남.
print("지금은 %d시 %d분입니다" % (hour,minute))

# =============== divmod  ===============
d, m = divmod(7, 3)  # 내장함수 : 7과 3을 가지고 몫과 나머지를 튜플로 만들어줌. = 에의해 언패킹일어나서 각각 들어감.
print("몫", d)
print("나머지", m)