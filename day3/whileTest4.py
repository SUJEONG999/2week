import random    # random 모듈을 가져옴
dice_num = random.randint(1, 6)
print("추출된 주사위 값 :", dice_num)
while dice_num > 4 :
    print("ㅋㅋ")   # ㅋㅋ가 계속 출력됨.
print("종료!!")