score = [ 88, 95, 70, 100, 99 ]
for no, s in enumerate(score, 1):  # 1부터 순서값매김
    print(str(no) + "번 학생의 성적 :", s)

names = "둘리,고길동,희동이,마이콜,또치,도우너"
namelist = names.split(",")  #데이터가 각각 리스트의 요소가 됨.
print(namelist)
namelist.sort()  # 먼저, sort 함.
for num, name in enumerate(namelist) :
    print(f"이름순으로 {name}는 {num+1}번입니다.")
for data in enumerate(namelist) :   # 튜플의 형태로 들어감.
    print(f"enumerate를 적용한 결과 : {data}")
for num, name in enumerate(namelist, 100) :  # 100부터 순서값 매김.
    print(f"이름순으로 {name}는 {num}번입니다.")



