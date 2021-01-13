listv1 = ["A", "b", "c", "D", "e", "F", "G", "h"]
listv2 = [i for i in listv1 if ord(i)>96]   # if 조건에 i.islower() 써도 됨.
print(listv2)