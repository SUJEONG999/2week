def normalfn(p1, p2, p3) :
    print(p1)
    print(p2)
    print(p3)
    print("-" * 10)

normalfn(10,20,30) # 포지션 아규먼트  : 정의된 위치에 따른 매핑
normalfn(p3=10,p1=20,p2=30) # 키워드 아규먼트 : 쌍을 이뤄서 매핑함. 작성되는 순서는 중요하지 않음. 매개변수이름(name value, key value)=값.
#normalfn("abc", "def") # 실행하면 error 남 : 매개변수 3개인데 2개만 주면 안된다.
#normalfn()  # 매개변수 3개인데 지정안해서 error남.

