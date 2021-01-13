s1="pythonjavascript"
print(len(s1))


s2 = "010-7777-9999"
print(s2.replace('-', ''))


s3 = "PYTHON"
print(s3[::-1])

s4 = "Python"
print(s4.lower())

s5 = "https://www.python.org/"
print(s5[8:-1:1])

s6 = '891022-2473837'
if s6[7]== '1' or s6[7] =='3':
    print('남자')
elif s6[7]== '2' or s6[7] =='4':
    print('여자')

s7='100'
print(int(s7))
print(float(s7))

s8 = 'The Zen of Python'
print(s8.count('n'))
print(s8.index('Z'))
print((s8.upper()).split(" "))