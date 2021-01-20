hap = 0
for i in range(1,51):
    if i % 3==0 :
        if i % 5 == 0:
            continue
        else :
            hap = hap + i

print("결과 =",hap)