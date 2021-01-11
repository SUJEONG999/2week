a = set()   # 빈 세트형
b = set([1, 2, 3, 3,4])
c = {1, 4, 5, 6, 1, 4}
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = set((10,))
f = {100,}
print('a - ', type(a), a)
print('b - ', type(b), b)   # 중복 되진 않는 세트 출력
print('c - ', type(c), c)
print('d - ', type(d), d)  # 다양한 타입으로 구성된 리스트를 세트로 만든다.
print('e - ', type(e), e) # 튜플가지고 세트 만듦.
print('f - ', type(f), f)
# for 문으로 데이터 추출
for data in d :
    print(data)

# 튜플 로 변환
t = tuple(b) # 세트 b를 튜플로 변환함
print('tuple - ', type(t), t)
print('tuple - ', t[0], t[1:3])

# 리스트로 변환
l = list(c)
print('list - ', type(l), l)
print('list - ', l[0], l[1:3])

print("----set 의 집합 연산----")
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1, s2)
print('intersect - ', s1 & s2)   # 교집합
print('union - ', s1 | s2)  # 합집합
print('difference - ', s1 - s2)  # 차집합
print('exclusive - ', s1 ^ s2)   # 각자 갖고 있는 거만 , 배타적인 데이터들

print("----추가 & 제거 & 갯수 채크----")
s1 = set()
s1.add(10);s1.add(20);s1.add(30);s1.add(40);s1.add(50)
print('s1(10,20,30,40,50추가) - ', s1)
s1.add(10)  #add : 하나씩 추가
print('s1(10추가실패) - ', s1)   # 있으니깐 넣어주지 않음
s1.update([40,50,60,70])   # update : 한꺼번에 여러개를 추가
print('s1(40,50,60,70변경) - ', s1)  # 중복 제외해서 추가
s1.remove(30)      # 요소 제거
print('s1(30삭제) - ', s1)
print('length - ', len(s1))  # 갯수 출력