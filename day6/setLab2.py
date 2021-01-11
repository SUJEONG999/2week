import random

set1 = set()

while True:
    set1.add(random.randint(1, 45))
    if len(set1)==6:  # 세트는 중복되면 add 되지 않음.
        break

print( "행운의 로또번호 :", set1)
print( "행운의 로또번호 :",", ".join( repr(e) for e in set1) )