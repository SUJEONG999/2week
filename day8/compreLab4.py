import random
randlist = [random.randint(0,100) for _ in range(10)]   # _ : 데이터셋에서 꺼내는데 실제 리스트가 만들어지는데 있어서 앞에서 변수명 안써서 _씀
print(randlist)

dic_p_np = { (randlist.index(e)+1): 'pass' if e > 60 else 'nopass' for e in randlist}
print(dic_p_np)


# 다른 학우 답안
# import random
# n =[]
# for i in range(0,11):
#   n.append(random.randint(0,100))
# print(n)
# d = i+1 : 'pass' if n[i] > 60 else 'nopass' for i in range(10)}