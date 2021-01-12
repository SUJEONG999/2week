def myprint (*args, **kwargs):
    if len(args) ==0 :
        print("Hello Python")
    else:
        deco = kwargs.get ('deco',"**")
        sep = kwargs.get ('sep',',')
        '''deco = "**"          
        sep = ","          
        if 'deco' in kwargs.keys():
            deco = kwargs['deco']
        if 'sep' in kwargs.keys():
            sep = kwargs['sep']'''
        print(deco,sep.join(str(data) for data in args),deco,sep="")

myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
myprint()
