import random
count = 0
while True:
    i = random.randint(0, 30)

    if 1 <= i <= 26:
        count = count + 1
        print(chr(i+64),"(",i,")")
    else :
        break

print("수행횟수는", count, "번입니다")