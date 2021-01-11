print("-- 슬라이싱 --")
nums = [0,1,2,3,4,5,6,7,8,9]
print(nums[2:5])  # 3번째 원소부터 5번째 원소까지
print(nums[:4])  # 첫번째 원소 부터 4번째 원소까지
print(nums[6:])
print(nums[1:7:2]) # 2번째 원소, 네번째 원소, 6번째 원소
print("-- 인덱스를 사용한 대입 --")
score = [ 88, 95, 70, 100, 99 ]
print(score[2])
score[2] = 55  # 3번째 원소를 55로 바꿈
print(score)
score[2] = [55, 66]  # 3번째 원소가 서브리스트로 들어감.
print(score) # 3번째 요소만 두개의 요소의 값으로 구성된 리스트가 생김
print("-- 슬라이싱을 사용한 대입 --")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)  # 리스트 만든 다음에 출력
nums[0:0] = [100] # [0], [0:1] : 첫번째 원소값을 100으로 바꿈, 그런데 [0:0] start = end 인경우 대체가 아닌 맨 앞에 껴놓겠다.
print(nums)
nums[2:5] = [20, 30, 40]  # 3번째 원소부터 5번째원소[1,2,3] 자리에 20, 30, 40이 대신 들어감.
print(nums)
nums[6:8] = [90, 91, 92, 93, 94]  # 7번째 원소부터 8번째 원소 자리에 빼서 90, 91, 92, 93, 94 끼워넣음
print(nums)
print("-- 슬라이싱을 사용한 제거 --")
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)
nums[2:5] = []   # 3번째 원소부터 5번째 원소를 잘라냄
print(nums)
del nums[4]  # 특정 요소를 잘라냄. 5번째 원소 잘라냄
print(nums)
print("-- 리스트 연산 --")
list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
listadd = list1 + list2  # 리스트끼리 결합하게 됨.
print(listadd)
listmulti = list2 * 3  # 리스트에 곱하기 3하면 3번 반복해서 리스트로 나옴.
print(listmulti)