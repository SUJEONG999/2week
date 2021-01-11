list= [[10, 12, 14, 16], [18, 20, 22, 24], [26, 28, 30, 32],[34, 36, 38, 40]]

print("1행 1열의 데이터 :", list[0][0])
print("3행 4열의 데이터 :", list[2][3])
print("행의 갯수 :", len(list))
print("열의 갯수 :", len(list[0]))   # 어느행을 기준으로 하든 상관없음
print("3행의 데이터들 :",list[2][0], list[2][1], list[2][2], list[2][3])
print("2열의 데이터들 :",list[0][1], list[1][1], list[2][1], list[3][1])
print("왼쪽 대각선 데이터들 :", list[0][0], list[1][1], list[2][2], list[3][3])
print("오른쪽 대각선 데이터들 :", list[0][3], list[1][2], list[2][1],list[3][0] )



print("3행의 데이터들 :",' '.join( repr(e) for e in list[2]))
col2 = []
for row in range(len(list)):
    col = 1
    col2.append(list[row][col])

print("2열의 데이터들 :",' '.join( repr(e) for e in col2))

diagonal1 = []
for row in range(len(list)):
    col = row
    diagonal1.append(list[row][col])

print("왼쪽 대각선 데이터들 :",' '.join( repr(e) for e in diagonal1))
diagonal2 = []
for row in range(len(list)):
    col = len(list) - row - 1
    diagonal2.append(list[row][col])

print("오른쪽 대각선 데이터들 :",' '.join( repr(e) for e in diagonal2))