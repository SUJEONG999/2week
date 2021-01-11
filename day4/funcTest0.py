def a() :
    pass   # 아무것도 수행하지 않겠다는 뜻(정의할 코드가 없을 때)
            # none 이 리턴됨

def b() :
    return '올라프'  #b를 호출하면 올라프 리턴됨

def c(p) :
    return p * 3    #p라는 매개변수에 반드시 데이터 전달해야하고, 3을 곱한 값 리턴

# 변수에 저장
result1 = a()     # 함수정의가 먼저 되어있어야한다. 그래야 호출 가능
result2 = b()
result3 = c('올라프') # 문자열일 때는 주어진 숫자만큼 반복(올라프를 입력받아서 3번 반복)
result4 = c(10)  # 숫자일 때는 곱셈 연산
#출력
print(result1)
print(result2)
print(result3)
print(result4)
print('----------------------')
print(a()) # 함수 저장없이 바로 출력
print(b())
print(c('둘리'))
print(c(20))


