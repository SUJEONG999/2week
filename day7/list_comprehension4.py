list1 = [ chr(d)  for d in range(ord('A'), ord('Z')+1) ]
print(list1)

list2 = [ d  for d in range(1, 16) ]
print(list2)

list3 = [ d  for d in range(1, 16) if not d % 2 ]  # 짝수인 경우
print(list3)

list4 = [ d  for d in range(1, 16) if not d % 3 ]  # 홀수인 경우
print(list4)

list5 = [ d   if d % 2  else  '짝수' for d in range(1, 16)  ]  # 홀수는 추출, 그렇지 않으면 짝수라는 문자를 쓰겠다.
print(list5)

list6 = [ '홀수'   if d % 2  else  '짝수' for d in range(1, 16)  ] # 홀수는 홀수라고하고, 그렇지 않으면 짝수라고 하겠다.
print(list6)

list7 = [ 'pass_'+str(d)   if d % 2  else   'fail_'+str(d) for d in range(1, 16)  ]   # 홀수면 pass_ 붙여서 쓰고, 짝수면 fail_ 써라
print(list7)

oldlist = [1, 2, 'A', False, 3]

newlist = [i * i for i in oldlist if type(i) == int]  # 정수형 숫자형만 뽑아내서 제곱하겠다.

print(newlist)



