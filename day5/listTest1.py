# 리스트
# 리스트 자료형(순서, 중복, 수정, 삭제)
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 10, 'Pen', 'Cap', 'Plate']  # 다양한 자료형의 데이터를 저장할 수 있음
e = list('유니코')
f = [10]

print("리스트데이터의 타입")
print(type(d), d, sep="--->") # 리스트 타입, 리스트에 대한 내용을 출력함.

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

print("리스트데이터의 길이")
print(len(a))
print(len(d))

print("리스트데이터의 인덱싱")
print('d - ', d[1])   # 두번째 원소값
print('d - ', d[0] + d[1] + d[1])  # 첫번째 원소 + 두번째 원소 + 두번째 원소 = 30
print('d - ', d[-1])  # 마지막 원소값

# 슬라이싱
print('d - ', d[0:3])   # 0,1,2 가 적용되어 첫번째 원소부터, 세번째 원소까지 (end index는 포함x)
print('d - ', d[2:]) # 3번째 원소부터 끝까지

print(d)
d[1] = 20  # 두번째 원소값을 20으로 바꿈.
print(d)

for e in d :  # 리스트 d 중에서 하나씩 출력
    print(e)