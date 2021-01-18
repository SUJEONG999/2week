try:
    print("네트워크 접속")
    a = 2 / 0  # 주석처리하면 예외 발생x
    print("네트워크 통신 수행")
except ZeroDivisionError as z : # ZeroDivisionError 발생하면 z에 담아라.
    print(z)
    '''import sys
    sys.exit(-1)  # 프로그램 중단시키더라도 finally 블럭은 수행시키고 중단시켜라.'''
finally:
    print("접속 해제")
print("작업 완료")