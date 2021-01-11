def differtwovalue(num1,num2):
    differ = abs(num1-num2)
    if num1 != num2:
        return differ
    else:
        return 0



import random
for i in range(5):
    n1 = random.randint(1, 30)
    n2 = random.randint(1, 30)

    print(n1, "와",n2,"의 차는", differtwovalue(n1,n2),"입니다.")