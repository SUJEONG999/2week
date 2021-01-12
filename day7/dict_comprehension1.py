students = dict(둘리=90, 또치=85, 도우너=95, 희동이=75, 마이콜=80)  # 딕셔너리 생성
print(students)

pass_students = { k : v for k, v in students.items()}  # 꺼낸 것을 가지고 키는 키 ,value는 value로
print(pass_students)

pass_students = { k : v for k, v in students.items() if v > 80}  # value가 80보다 큰 값만 키는 키 ,value는 value로
print(pass_students)

pass_students = { k : v for k, v in students.items() if len(k) > 2}  # 키의 길이가 2보다 큰 값만 키는 키 ,value는 value로
print(pass_students)

pass_students = { k : v for k, v in students.items() if len(k) > 2 and v > 80}   # 키의 길이가 2보다 크고 value가 80보다 큰 값만 키는 키 ,value는 value로
print(pass_students)

swap_students = { v : k for k, v in students.items() }   # key와 value를 서로 바꿈.
print(swap_students)

