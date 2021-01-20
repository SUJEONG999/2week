import time
import datetime
print(__name__ +"모듈 : "+ str(datetime.datetime.now())) # main으로 실행
time.sleep(3) # 3초 쉬었다가
import B # B 모듈을 데리고 들어오고 실행함.
time.sleep(3)
import C # if __name__ == "__main__": 가 있어서 수행 안됨.
time.sleep(3)
import D
time.sleep(3)
print(__name__ +"모듈 : "+ str(datetime.datetime.now())) # main으로 실행