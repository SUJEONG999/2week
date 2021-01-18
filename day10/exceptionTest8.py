dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
#방법1
try:
    print(dic['girl']) # girl 이라는 키를 갖는 value 값을 꺼내겠다.
except:
    print("찾는 단어가 없습니다.")

#방법2
han = dic.get('girl')
if (han == None):
    print("찾는 단어가 없습니다.")
else:
    print(han)
