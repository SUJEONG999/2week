def calcscore(name, *score, **option): #  일반인수, 가변인수, 키워드 가변인수 순으로 써야함.
    print(name)
    sum = 0
    for s in score:
        sum += s
    print("총점 :", sum)
    if (option['avg'] == True ):  # avg 라는 키워드 아규먼트  , 이렇게 썼을 경우라면 avg = 반드시 써줘여함.
        print("평균 :", sum / len(score))


calcscore("김상형", 88, 99, 77, avg = True)
calcscore("김한슬", 99, 98, 95, 89, avg = False)  # 평균을 제외한 나머지 결과만 나옴
calcscore("둘리")  # 둘리 이름 나오고 총점 0 나오지만 실행오류 나옴