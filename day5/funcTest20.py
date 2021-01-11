print("---가변형 인자 함수 정의---")
def sumall(*p) :  # 매개변수앞에 *주면 아규먼트를 0개이상 받을 수 있는 변수다. 아규먼트를 원하는 만큼 전달해라.
    """ 아규먼트로 전달되는 모든 숫자들의 합을 리턴"""
    print("p의 타입 :", type(p))
    sum = 0
    for data in p :
        sum += data
    return sum

print(sumall(1,2,3,4,5)) # 아규먼트가 5개 됨.
print(sumall(100, 200, 300))
print(sumall(10,20,30,40,50,60,70))
print(sumall())

help(sumall)