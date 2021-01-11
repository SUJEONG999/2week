mammal = { '코끼리', '고릴라', '사자', '고래', '사람', '원숭이', '개' }
primate = { '사람', '원숭이', '고릴라' }

if '사자' in mammal:
    print("사자는 포유류이다")
else:
    print("사자는 포유류가 아니다.")

# 세트에서는 포함관계를 체크하는 연산자로 쓰임  책 : p 238
print(primate <= mammal)    # 부분집합 기호 , 왼쪽이 오른쪽의 부분집합인지
print(primate < mammal)   # 진성 부분집합 , 부분집합이면서 여분의 원소가 더있음
print(primate <= primate)
print(primate < primate)

