def asterisk_test(a, **kargs) :
    print(a, kargs)
    print(type(a), type(kargs))
    print(kargs.keys())
    print(kargs.values())
    print(kargs.items())
    for key, value in kargs.items() :
        print(key, value, sep="->")

asterisk_test(a=1, b=2, c=3, d=4, e=5, f=6)
print("-"*50)
asterisk_test(100, v1=100, v2=200)
print("-"*50)
asterisk_test(1000)