# 일부 기본값(디폴트) 매개변수
def defaultfn2(p1, p2="abc", p3=True) :  # p2, p3는 기본값으로 갖고 있는 매개변수로 설정
    print(p1)
    print(p2)
    print(p3)
    print("=" * 10)

defaultfn2(10,20,30)   # 기본값무시하고 설정한 값으로 추출
defaultfn2("abc", "xyz") # p1= abc, p2 = xyz, p3= 기본값으로 추출
defaultfn2(p2="가", p1="xyz")
defaultfn2("aa")  # p1= aa로 지정됨.
defaultfn2(p1="올라프")
defaultfn2()  # 최소한 p1은 필요한데 (필수매개변수) 아규먼트 지정이 안되어서 오류 뜸
