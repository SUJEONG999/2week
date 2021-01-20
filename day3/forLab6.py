hap = 0
for i in range(3,51,3):  # range(1,51)
    if i % 5 == 0:   # if i%3==0:
        continue        # if i%5==0:
    else :            #continue
        hap = hap + i

print("결과 =",hap)