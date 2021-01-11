maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
print(maria)
average = sum(maria.values()) / len(maria)
print(average)


list1 = [ ['boy', '소년'], ['school', '학교'], ['book', '책'] ]  # 3행 2열 데이터
dic = dict(list1)
print(dic)

list2 = [ ('boy', '소년'), ('school', '학교'), ('book', '책') ]
dic = dict(list2)
print(dic)

list3 = dict(boy= '소년', school='학교', book='책')  # 함수로 딕셔너리 만듦
dic = dict(list3)
print(dic)


x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x)

item = x.items()
# for key, value in item:  # item 에서 하나씩 꺼내서 값을 변경할 때 list로 만들어서 해야함.
#     if value == 20:
#         del x[key]
print(list(item))
for key, value in list(item):
    if value == 20:
        del x[key]

print(x)