class Student :
   '''
   학생 객체를 생성할 수 있는 Student 클래스입니다.
   인스턴스 생성시에는 학생의 이름, 나이, 과목명을 전달하세요.
   '''
   def __init__(self, name, age, subject): # 객체 초기화 메서드, 객체 만의 변수(멤버 변수)들을 생성함.
       self.name = name # 독스트링 : 맨앞에 와야함.
       self.age = age
       self.subject = subject

   def printStudentInfo(self):
       print("{}의 나이는 {}세입니다.".format(self.name, self.age))

   def study(self):
       print("{} 학생은 {} 과목을 학습합니다.".format(self.name, self.subject))


st1 = Student("둘리", 10, "파이썬")  # 3개의 아규먼트 전달.
st2 = Student("도우너", 12, "자바") # 생성자 함수( 클래스 이름에 괄호 붙인것)
st3 = Student("또치", 10, "자바스크립트")

st1.printStudentInfo() # 둘리객체의 이름과 나이 값을 형식에 맞춰서 출력
st2.printStudentInfo() # 객체에 대한 참조값
st3.printStudentInfo()

st1.study()
st2.study()
st3.study()

print("\n[ st2=st1 과 st3=st1 연산 수행 ]")
st2 = st1   # 대입
st3 = st1

st1.printStudentInfo()
st2.printStudentInfo()
st3.printStudentInfo()

help(Student)