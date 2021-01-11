def print_triangle_withdeco(num,deco ='%'):
        if 1 <= num <= 10:
            for i in range(1, num + 1):
                print(" " * (num - i), end="")
                print(deco * i)
        else:
            pass  # 이때는 else문을 자체 생략해도 됨.

print_triangle_withdeco(2)
print()
print_triangle_withdeco(5,'*')
print()
print_triangle_withdeco(11)