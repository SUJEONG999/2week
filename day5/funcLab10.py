def sumAll(*p):
    count=0
    ans =0
    for i in p:
        if type(i) == int:
            count+=1
            ans+=i
        else:
            pass
    if len(p) == 0 or count == 0:
        ans = None
    return ans




print(sumAll(1, 2, 3))
print(sumAll(100, 'a', '*'))
print(sumAll())
