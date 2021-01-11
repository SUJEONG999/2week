# 기본값(디폴트) 매개변수
def defaultfn1(p1=10, p2="abc", p3=True) :   # 매개변수 미리 세팅함. : 기본값 매개 변수 또는 디폴트 매개변수라고 한다.
    print(p1)
    print(p2)
    print(p3)
    print("=" * 10)

defaultfn1(10,20,30)  # 기본값무시하고 전달된 값으로 추출
defaultfn1("abc", "xyz")  # 전달된 값과 기본값 추출
defaultfn1(p2="가", p1="xyz", p3="P")  # 기본값무시하고 전달된 값으로 추출
defaultfn1()  # 아무것도 안주어서 기본값으로 추출

