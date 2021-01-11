import math
while True:
    number = int(input("숫자 하나를 입력하시오 :"))
    if number == 0:
        print("종료")
        break
    elif number < -10 or number > 10:
        continue
    elif number >0:
        print("입력값 :", number)
        print(math.factorial(number))

    else:
        print("입력값(부호변경) :", -number)
        print(math.factorial(-number))