def sumEven1(*num) :
    sum = 0
    for data in num:
        if data % 2 == 0:
            sum += data

    if len(num) == 0:
        sum = -1
    return sum


print(sumEven1(1,2,3,4,5))
print(sumEven1())
print(sumEven1(3,5))