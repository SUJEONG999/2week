hap = 0
for i in range(1,51):
    if  i%3 == 0 and i%5!=0:
        hap = hap + i

print("결과 =",hap)
