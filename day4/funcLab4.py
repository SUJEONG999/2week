def print_triangle(n):
    if 1 <= n <= 10:
        for i in range(1,n+1):
            print('*'*i)
    else:
        pass     # 이때는 else문을 자체 생략해도 됨.

print_triangle(2)
print()
print_triangle(5)
print()
print_triangle(11)