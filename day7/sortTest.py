# =============== sort  ===============
score = [ 88, 95, 70, 100, 99 ]
score.sort()
print(score)
score.reverse()
print(score)

# =============== sort2  ===============
country = ["Korea", "japan", "CHINA", "america"]
country.sort()   # 문자열 가지고 sort 함. 대문자 < 소문자, 알파벳 순
print(country)
country.sort(key = str.lower)  #모두다 소문자로 바꿔서 sorting
print(country)

# =============== sort3 ===============
country = ["Korea", "japan", "CHINA", "america"]
country.sort()
print(country)
country.sort(key = len)   # 길이 정보를 가지고 sorting 하겠다. 깉이가 같다면 알파벳순(대문자<소문자)
print(country)

# =============== sorted  ===============
score = [ 88, 95, 70, 100, 99 ]
score2 = sorted(score)
print(score)    # 이때 score 원본은 그대로(변화x)
print(score2)