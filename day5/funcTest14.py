price = 1000   # 전역 변수 price를 초기화함.

def sale():          # 함수 정의
    global price        # 이 함수내에서 값을 할당하는 price 는 전역 변수라고 설정하는 결과가 된다.
    price = 500         # 전역변수 price 의 값을 변경하게 된다. (전역변수 price에서 넣으시오)
    print("sale", price)   # sale함수 내에서 수행해봄.

sale()
print("global", price)    # sale함수 수행하고나서 밖에서 수행해봄.(둘다 500)

price = 1000

def sale():
    global price
    price = 500

sale()
print(price)
