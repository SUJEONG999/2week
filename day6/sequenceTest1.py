s1 = "abcdefgh1abcaa234가나다"
print(s1)
print("---in과 not in 연산자---")
print('a' in s1)
print('a' not in s1)
print('가나' in s1)
print('가다' not in s1)  # 연이어져서 나와야 TRUE
print("---시퀀스연산---")
s2 = "파이썬"
print(s1+s2)
print(s1)
print(s2)
print(s2 * 3)
print("---인텍싱과 슬라이싱---")
print(s2[0]); print(s2[1]); print(s2[2]); print(s2[-1])
print(s1[:])
print(s1[::1])
print(s1[::2])
print(s1[::-1])
print(s1[0:4:1])  # 첫번째 문자부터 4번째 문자까지
print("---함수들---")
print(len(s1))   # 갯수
print(max(s1)); print(min(s1))  # 코드값 크기 : 숫자<영문<한글
print(s1.count('a'))  #a가 몇개 들어있느냐
print(s1.count('abc'))
print("---for와 함께 사용하는 시퀀스---")
for data in s2 :
    print("#", data, "#")
#print("---문자열은 변경불가---")
#s2[0] = "가"
