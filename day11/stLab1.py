import calendar
while True:
    year = input("년도를 입력하세요 : ")
    month = input("월을 입력하세요 : ")
    try:
        x = int(year)
        y = int(month)
        calendar.prmonth(x, y)
        break
    except ValueError:
        print("숫자로 다시 입력해주세요")