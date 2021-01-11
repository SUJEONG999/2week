def print_gugudan(n):
    if type(n) != int :
        return
    elif n <1 or n >9:
        return
    else:
        print(n, "단")
        for hang in range(2,10):
            print(n, "*", hang, "=", n * hang)
        print()


print_gugudan(5)