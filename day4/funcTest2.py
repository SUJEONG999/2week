def calcrange(begin, end):  # 시작값과 종료값까지의 합산
    sum = 0
    for num in range(begin, end + 1):
        sum += num
    return sum

print("3 ~ 7 =", calcrange(3, 7))


