import random
evensum = 0
x = random.randint(1, 10)
y = random.randint(30, 40)

for d in range(x, y+1):
    if d % 2 == 0:
        evensum += d
print(x,"부터",y, "까지의 짝수의 합 :",evensum)
