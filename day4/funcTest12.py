def kim():
    temp = "김과장의 함수" # 지역변수 : 함수 안에서 만들어진 변수
    print(temp)   # cf. 전역변수 : 함수 밖에서 만들어진 변수

def lee():
    temp = 2 ** 10
    return temp

def park(a):
    temp = a * 2
    print(temp)

kim()
print(lee())
park(6)
# print(temp)
# 위를 실행하면 temp 변수를 정의하지 않고 출력하겠다고 해서 오류남.
# 현재 temp는 지역변수라서 함수 외부에서는 쓸수 없다.
