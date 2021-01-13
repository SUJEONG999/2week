def updatelist(times, listnums) : # 첫번째 아규먼트는 숫자 받고, 두번째 아규먼트는 리스트 받음
    for i in range(len(listnums)) : # 리스트 개수만큼 돌려서
        listnums[i] *= times  # 리스트의 요소마다 숫자를 곱함.


l1 = [1,2,3,4,5]
print(l1)   # 함수 호출전
updatelist(2, l1)   # 함수에의해 공유된 리스트의 요소마다 2를 곱해줌   # 만약, l1,copy()로 불러왔으면 l1 변화 없음.
print(l1)   # 리스트가 변경됨.
print("-"*10)
l2 =  [10, 20, 30, 40];
print(l2)  # 함수 호출전
updatelist(3, l2)  # 함수에의해 공유된 리스트의 요소마다 3을 곱해줌
print(l2)

