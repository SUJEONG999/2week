dictionary = {}  # 비어있는 딕셔너리

print("요소 추가 이전:", dictionary)

dictionary["name"] = "새로운 이름"   # 새로운 데이터를 넣어줌
dictionary["head"] = "새로운 정신"  # 존재하지 않는 키들이라서 새로 추가됨
dictionary["body"] = "새로운 몸"

print("요소 추가 이후:", dictionary)

dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임"
    }

print("요소 제거 이전:", dictionary)

del dictionary["name"]     # 이미 존재하는 요소 삭제하는 경우
del dictionary["type"]

print("요소 제거 이후:", dictionary)