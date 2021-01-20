import sys
sys.path.append("C:/PyStudy")

from mypack.calc import *
add.outadd(1,2)
multi.outmulti(1,2)

# 가능하지만 권장되지는 않는 방법
'''from mypack.report.table import *  # from에 모듈명까지 주고 모든 함수들을 import 하는 것
outreport()
a()
b()
c()'''