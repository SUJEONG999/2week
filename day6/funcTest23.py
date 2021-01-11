def getlist1(times, *nums) :
    newnums = []   # 비어있는 리스트 생성
    for data in nums :
        newnums.append(data * times)
    return newnums

print(getlist1(2, 1,2,3,4,5))    # 1,2,3,4,5를 각각 2를 곱해서 나오는 값
print(getlist1(3, 1,2,3,4,5,6,7))  # 숫자하나와 가변인수들 전달하면 각각 곱해서 나오게 됨.
# 첫번째는 무조건 times에 나머지는 무조건 nums로!

def getlist2(times, *nums) :
    newnums = list()
    for data in nums :
        newnums.append(data * times)
    return newnums

print(getlist2(2, 1,2,3,4,5))
print(getlist2(3, 1,2,3,4,5,6,7))

