def expr(num1, num2, cal):
    if cal == "+":
        ans = num1 + num2
    elif cal == "-":
        ans = num1 - num2
    elif cal == "*":
        ans = num1 * num2
    elif cal == "/":
        ans = num1 / num2
    else:
        ans = None
    return ans

result = expr(3,5,"+")
if result == None:
    print("수행 불가")
else:
    print("연산결과 :",result)

result = expr(3,5,"#")
if result == None:
    print("수행 불가")
else:
    print("연산결과 :",result)