listnum =[]
import random
for i in range(10):
    listnum.append(random.randint(1, 50))

print(listnum)

for y in listnum:
    if y < 10:
        listnum[listnum.index(y)]= 100

# 대신에 for x in range(10):
#    if listnum[x] < 10:
#       listnum[x] = 100

print(listnum)

print(listnum[0])
print(listnum[-1])  # 대신에 listnum[len(listnum)-1]
print(listnum[1:6])
print(listnum[-1:-21:-1])  # 대신에 listnum[::-1]
print(listnum[:])
del listnum[4]
print(listnum[:])
listnum[1:3] = []
print(listnum[:])
