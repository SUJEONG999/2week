def func1(n) :
    return n * 2

def func2() :
    print("func2 호출 - hello")

print(type(func1))
print(type(func2))
print(func1(10))
print(func2()) # 자동으로 프린트가 되는데 리턴 결과가 없으므로 None 도 출력됨.

print("=" * 20)
print(func2)
v = func2  # v변수에 저장하여 같이 공유하게 됨.
print(v)
v() # func2 호출됨.

def say1() :
    print("안녕?")

def say2() :
    print("Hello?")

print("=" * 20)
#아규먼트로 함수 전달
import types
def callback(fn) :
    if type(fn) == types.FunctionType : # 어떤 담겨져있는 변수가 함수인지 확인
        fn()  # 매개변수이름으로 전달된 함수를 실행하겠다.
    else :
        print("아규먼트로 함수를 주세요")

callback(say1)
callback(say2)
callback(100)



