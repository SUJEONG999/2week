class Member :
    def __init__(self):
        self.name = None
        self.account = None
        self.passwd = None
        self.birthtyear = None

m1 = Member()
m2 = Member()
m3 = Member()

m1.name = "강호동"
m1.account = "id1"
m1.passwd = "1234"
m1.birthtyear = 1970

m2.name = "유재석"
m2.account = "id2"
m2.passwd = "4567"
m2.birthtyear = 1972

m3.name = "신동엽"
m3.account = "id3"
m3.passwd = "8910"
m3.birthtyear = 1971


print(f" 회원1 : {m1.name}({m1.account},{m1.passwd},{m1.birthtyear})")
print(f" 회원2 : {m1.name}({m1.account},{m1.passwd},{m1.birthtyear})")
print(f" 회원3 : {m1.name}({m1.account},{m1.passwd},{m1.birthtyear})")