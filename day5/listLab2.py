listnum = [10, 5, 7, 21, 4, 8, 18]

def find_min(a):
    n = len(a)  # 입력 크기 n
    min_listnum = a[0]  # 리스트 중 첫 번째 값을 일단 최솟값으로 기억
    for i in range(1, n):  # 1부터 n - 1까지 반복
        if a[i] < min_listnum:  # 이번 값이 현재까지 기억된 최솟값보다 작으면

            min_listnum = a[i]  # 최솟값을 변경

    return min_listnum


print("최솟값 :",find_min(listnum))