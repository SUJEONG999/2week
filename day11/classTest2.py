class Student :
   def __init__(self):
       print("인스턴스 생성!!")

   def __del__(self):
       print("인스턴스 삭제!!")

st1 = Student()  # 객체 생성
st2 = Student()
st3 = Student()

print(type(st1), st1)
print(type(st2), st2)
print(type(st3), st3)

print("[ st1이 참조하고 있는 Student 인스턴스 삭제]")
del st1 # st1 을 없애겠다.

print("종료")
# 자동으로 종료되면서 객체 상태가 해제되면서 자동으로 호출된다.