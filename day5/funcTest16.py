def calcsum(n):
    """1 ~ n까지의 합계를 구해 리턴한다."""  # 도큐먼트 주석 (docstring) :함수 정의하고 주석달 때 (함수 설명 닮)
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

print(calcsum(10))
help(calcsum)  # 함수에 대한 설명글 도출됨.

