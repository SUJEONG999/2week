print("-- 중첩 리스트1 --")
lol = [ [1, 2, 3], [4, 5], [6, 7, 8, 9]]  # 파이썬에서는 행마다 열의 개수를 다르게 지정할 수 있음
print("이차원 리스트 인덱싱[행][열]")
print(lol[0])  # 행 인덱스임 , 1행
print(lol[2][1]) #  3행 2열
print("이차원 리스트의 행 갯수와 각 행마다의 열 갯수")
print(len(lol))  # 이차원리스트에 len 하면 행갯수
print(len(lol[0])) # 첫번째 행에 len 하면 해당 열갯수
print(len(lol[1])) # 두번째 행에 lne 하면 해당 열갯수
print(len(lol[2]))
print("for문을 이용한 이차원 리스트 데이터 추출")
for sub in lol:  # lol에서 꺼내지는 데 첫번째 행(원소3개), 두번째행(원소2개), 세번째행(원소3개) 추출
    for item in sub: # 각각의 행마다 담겨져 있는 열의 개수 만큼 추출
        print(item, end=' ')
    print()

print("-- 중첩 리스트2 --")
score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
    ]

total = 0
totalsub = 0
for student in score:
    sum = 0
    for subject in student:
        sum += subject
    subjects = len(student)
    print("총점 :", sum, "평균 :", sum / subjects)
    total += sum
    totalsub += subjects
print("전체평균 :", total / totalsub)
