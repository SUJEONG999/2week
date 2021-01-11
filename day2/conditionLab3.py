import random
grade = random.randint(1, 6)

if grade >= 1 and grade<4 :
    print(str(grade), "학년은 저학년입니다.")

else:
    print(str(grade), "학년은 고학년입니다.")