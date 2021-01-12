def mydict (**kwargs):
    dic = {}
    for kw, args in kwargs.items():
        dic['my' + kw] = args
    return dic

print(mydict(Korean=50, Math=100, Science=30))
print(mydict())


