import random
listnum=[]

while True:
   x= random.randint(1, 45)
   if len(listnum) ==6:
       break
   if x not in listnum :
       listnum.append(x)

print( "행운의 로또번호 :",", ".join( repr(e) for e in listnum ) )