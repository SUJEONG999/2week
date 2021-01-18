str = "89점"
try:
    score = int(str)
    print(score)
except: # 어떤 예외가 발생하든 실행해라.
    print("예외가 발생했습니다.")
    import sys
    sys.exit(-1) # 프로그램 중단 명령 (0이 아니면 실행)
print("작업완료")