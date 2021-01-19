class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, money): # 추가로 받을 것이 있을 경우에는 뒤에 추가로 적어줌
        self.balance += money
    def inquire(self):  # 추가로 받을 것이 없기 때문에 생략
        print("%s의 잔액은 %s원입니다." % (self.name, format(self.balance, ',')))

obj1 = Account("둘리", 8000)
obj2 = Account("또치", 8000)
obj3 = Account("도우너", 8000)
obj1.deposit(1000)
obj2.deposit(2000)
obj3.deposit(3000)
obj1.inquire()
obj2.inquire()
obj3.inquire()

