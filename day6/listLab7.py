list=[[10, 20, 30, 40, 50], [5, 10, 15], [11, 22, 33, 44], [9, 8, 7, 6, 5, 4, 3, 2, 13]]


for i in range(4):
    print(i+1,"행의 합은", sum(list[i]), "입니다")

"""count = 1
while count <=4:
    for c in list:
        sum = 0
        for sub in c:
            sum += sub
        print( count ,"행의 합은", sum, "입니다")
        count+=1"""