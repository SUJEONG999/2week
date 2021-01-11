import random
score = random.randint(0, 100)

if score >= 90 and score <= 100 :
    t = "A"

elif score >= 80 and score <= 89:
    t = "B"

elif score >= 70 and score <= 79:
    t = "C"

elif score >= 60 and score <= 69:
    t = "D"

else:
    t = "F"

print(str(score), "점은 ",t,"등급입니다.")