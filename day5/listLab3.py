listnum = [10, 5, 7, 21, 4, 8, 18]
min_listnum = listnum[0]  # 리스트 중 첫 번째 값을 일단 최솟값으로 기억
min_listnum = listnum[0]
for i in range(1, len(listnum)):  # 1부터 n - 1까지 반복
    if listnum[i] < min_listnum:  # 이번 값이 현재까지 기억된 최솟값보다 작으면
        min_listnum = listnum[i]  # 최솟값을 변경

    elif listnum[i] > max_listnum:  # 이번 값이 현재까지 기억된 최댓값보다 크면

        max_listnum = listnum[i]  # 최댓값을 변경


print("최솟값 :",min_listnum,", 최댓값 :",max_listnum)





