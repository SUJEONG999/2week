score_tuples = [('math', 90), ('history', 80), ('english', 95), ('computer engineering', 100), ('science', 60)]  # 요소값들이 튜플임. 5개의 튜플
score_dict = dict(score_tuples)
print(score_dict)

score_dict = {t[0]: t[1] for t in score_tuples}  # 튜플의 첫번째 요소를 키, 튜플의 두번째 요소를 value
print(score_dict)

score_dict = {k : v for k, v in score_tuples}  # 언패킹이 일어나서 똑같이 딕셔너리 생성
print(score_dict)

score_dict = {k : v for k, v in score_tuples if len(k) > 5} # 길이가 5보다 큰 키만 해서 키와 value 생성
print(score_dict)

score_dict = {k : v for k, v in score_tuples if v >= 90}
print(score_dict)

score_dict = {k : v for k, v in score_tuples if v < 70}
print(score_dict)