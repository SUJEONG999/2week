oldlist = [17,2,14,6,10,19,16,12,5]
newlist1 = [ oldlist ]  # 이중리스트가 됨
print(newlist1)

newlist2 = list( [1,2,3,4,5,6,7,8] ) # 리스트함수 쓰면 리스트 생김
print(newlist2)

newlist3 = list( (1,2,3,4,5,6,7,8) ) # 튜플 전달 -> 리스트
print(newlist3)

newlist4 = list( {1,2,3,4,5,6,7,8} )  # 집합 전달 -> 리스트
print(newlist4)

newlist5 = list( "ABC") # 문자열 전달 -> 리스트
print(newlist5)

newlist6 = [ x for x in range(1, 9) ]  # 1~8 생성
print(newlist6)

newlist7 = [ x for x in oldlist if x % 2 ]   # 홀수인 경우만 추출
print(newlist7)

newlist8 = [ x for x in oldlist if x > 10 ]  # 10보다 큰 값만 추출
print(newlist8)

newlist9 = [ x*10 for x in oldlist if x < 10 ]  # 10보다 작은 건만 추출해서 곱하기 10
print(newlist9)

flowernames = ['rose', 'sunflower', 'tulip', 'magnolia', 'goldenbell', 'lily']
newlist10 = [i for i in flowernames if len(i) == 4]
print(newlist10)
