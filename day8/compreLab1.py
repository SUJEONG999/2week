def createList (*args, type=1):  # * : 패킹해서 받겠다
    if args :
        if type == 2:
            l = [e for e in args if not e % 2 ]
        elif type == 3:
            l = [e for e in args if e % 2 ]
        elif type == 4:
            l = [e for e in args if e > 10 ]
        elif type == 1:
            l = [e for e in args ]
    else :
        l = [n for n in range(1, 31)]
    return l

print(createList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,type=1))
print(createList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,type=2))
print(createList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,type=3))
print(createList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,type=4))
print(createList( ))


