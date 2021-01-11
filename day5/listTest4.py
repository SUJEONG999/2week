print("-- 리스트에 데이터 추가 --")
nums = [1, 2, 3, 4]  # 리스트 만들어서
print(nums)  # 출력
nums.append(5)  # 맨뒤에 5를 추가함 (하나 추가할 경우)
print(nums)
nums.insert(2, 99)  # 2에 해당하는 인덱스(3번째)에 99를 집어넣어서 밀려나게됨
print(nums)

print("-- 리스트에 범위를 지정하여 데이터 추가 --")
nums = [1, 2, 3, 4]
print(nums)
nums[2:2] = [90, 91, 92]   # [2:2] 는 index(3번째 자리)에 90,91,92를 추가한다.
print(nums)

nums = [1, 2, 3, 4]
nums[2] = [90, 91, 92]  # [2]는 3번째 자리에 또다른 리스트가 요소로 들어가게 된다.
print(nums)

print("-- 리스트 뒤에 또 다른 리스트 데이터 확장 --")
list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
list1.extend(list2)   # list1에 list2를 붙여서 확장해라. (여러개 추가할 경우)
print(list1)

print("-- 리스트의 데이터를 삭제하는 다양한 방법 --")
score = [ 88, 95, 70, 100, 99, 80, 78, 50 ]
score.remove(100)   # 값을 찾아서 삭제해라.
print(score)
del(score[2])  # 3번째 원소를 삭제 하시오
print(score)
score[1:4] = []   # 2번째 원소부터 4번째 원소까지 삭제하시오. (여러 원소 삭제)
print(score)

print("-- pop() 메서드로 ㄹ스트 데이터 지우고 꺼내기 --")
score = [ 88, 95, 70, 100, 99 ]
print(score.pop())   # () : 아무것도 없으면 마지막 요소를 지우고 꺼내온다.
print(score.pop())
print(score.pop(1))   # 2번째 지우고 꺼내온다.
print(score)

print("-- 리스트에서 데이터 위치(인덱스) 찾기와 갯수 카운팅 --")
score = [ 88, 95, 70, 100, 99, 80, 78, 50 ]
perfect = score.index(100)    # 주어진 리스트에서 이 값에 해당하는 index 추출
print("만점 받은 학생은 " + str(perfect) + "번입니다.")
pernum = score.count(100) # 리스트에서 갯수가 몇개 인지.!
print("만점자 수는 " + str(pernum) + "명입니다")

print("-- in 연산자를 사용하여 리스트에 데이터 존재여부 채크 --")
ans = input("결제 하시겠습니까? ")
if ans in ['yes', 'y', 'ok', '예', '당근']:
    print("구입해 주셔서 감사합니다.")
else:
    print("안녕히 가세요.")
