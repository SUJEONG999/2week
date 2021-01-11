while True:
    Month = int(input("월을 입력하시오(숫자만):"))
    if 1 <= Month <= 12:

        if Month == 12 or Month == 1 or Month == 2:
            print (Month, "월은 겨울",sep="")

        elif Month == 3 or Month == 4 or Month == 5:
            print(Month, "월은 봄",sep="")

        elif Month == 6 or Month == 7 or Month == 8:
            print(Month, "월은 여름",sep="")

        else:
            print(Month, "월은 가을",sep="")
    else :
        print("1~12 사이의 값을 입력하세요!")
        break