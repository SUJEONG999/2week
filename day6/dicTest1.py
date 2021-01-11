dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
print(dic)

print(dic['boy'])  # dic에서 boy 키를 갖는 value 값 출력
print(dic['book'])
#print(dic['student'])   # 없는 키를 꺼내라고 하면 실행 에러가 남.
print(dic.get('student'))   # dic.get 은 딕셔너리에 소속된 함수임. student 키를 갖는 value 값 출력
print(dic.get('student', '사전에 없는 단어'))  # 기본값 설정

if 'student' in dic:   # 키 체크
    print("사전에 있는 단어입니다.")
else:
    print("이 단어는 사전에 없습니다.")

dic['boy'] = '남자애'  # 변경
dic['girl'] = '소녀'  # 새로이 추가
del dic['book']  # 삭제
print(dic)