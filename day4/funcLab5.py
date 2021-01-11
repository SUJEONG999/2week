def print_triangle(n):
    if 1 <= n <= 10:
        for i in range(1,n+1):   # range(n,0,-1)
            print('@'*(n+1-i))   # print("*" * i)
    else:
        return

print_triangle(2)
print()
print_triangle(5)
print()
print_triangle(11)