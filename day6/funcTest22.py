def printdeco(*p, deco="@") :   # 일반인수, 가변인수, 키워드 가변인수 순으로 써야함.
    for data in p :            # 그러나 가변인수 뒤에 기본값을 가지고 있는 일반 변수는 올 수 있음
        print(deco, data, deco)
    print()

printdeco(1,2,3,4,5)
printdeco("가", "나")
printdeco(True, "A", 10, deco="$")
