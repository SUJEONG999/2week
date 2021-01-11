dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
print(dic.keys())  # 키 값 출력
print(dic.values()) # value 출력
print(dic.items())   # 키 와 value 쌍 출력

keylist = dic.keys()   # 하나 하나 꺼냄
for key in keylist:
    print(key)

valuelist = dic.values()
for value in valuelist:
    print(value)

itemlist = dic.items()
for item in itemlist:
    print(item)

itemlist = dic.items()
for key,value in itemlist:  # 꺼내진 튜플마다 언패킹이 일어나서 하나씩 들어감
    print(key, value, sep="-")