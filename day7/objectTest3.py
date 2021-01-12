import datetime

print([4,15,2,30,4].count(4))  # 이 리스트 안에 4라고 하는 데이터가 몇개 인지
listv = [4,15,2,30,4]  # 리스트를 변수에 담음
print(listv.count(4))  #변수.count : count 매서드 호출

now = datetime.date.today()  # 오늘날짜함수
print(now, type(now))
print(now.weekday()) #요일정보 메서드 : 숫자로 리턴(0월1화..)
print(now.ctime()) # 요일월일시분초년도 정보
print("===2021년 크리스마스===")
christmas = datetime.date(2021, 12, 25)
print(christmas, type(christmas))
print(christmas.weekday()) #토요일이 5
print(christmas.ctime())