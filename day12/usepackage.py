import sys
sys.path.append("C:/PyStudy") # 맨 뒤에 추가
print(sys.path)
import mypack.calc.add # mypack 패키지에 가서 calc 서브 패키지에가서 add 모듈을 쓰겠다.
mypack.calc.add.outadd(1,2) # add 모듈 안에 outdaaa 함수가 있는데 함수 실행

import mypack.report.table # mypack 패키지에 가서 report 서브 패키지에가서 table 모듈을 쓰겠다.
mypack.report.table.outreport()  # table 모듈 안에 outreport 함수가 있는데 함수 실행

# 방법2
import mypack.calc.add as my1 # 좀더 간단하게
my1.outadd(1,2)

import mypack.report.table as my2
my2.outreport()