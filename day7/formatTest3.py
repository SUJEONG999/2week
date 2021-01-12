# 파이썬 2.6 과 3.0부터 사용 가능
# =====newformat  =====
name = "한결"
age = 16
height = 162.5
print("이름:{}, 나이:{}, 키:{}".format(name, age, height))

# =====newformat2  =====
name = "한결"
age = 16
height = 162.5
print("이름:{0:s}, 나이:{1:d}, 키:{2:f}".format(name, age, height))  # 숫자는 아규먼트 순서를 의미함.

# =====newformat3  =====
name = "한결"
age = 16
height = 162.5
print("이름:{0:10s}, 나이:{1:5d}, 키:{2:8.2f}".format(name, age, height))
#폭은 10이고 문자야.  폭은 5이고 숫자야.  폭은8이고유효자리수는2이고 실수야.

# =====newformat4  =====
name = "한결"
age = 16
height = 162.5
print("이름:{0:^10s}, 나이:{1:>5d}, 키:{2:<8.2f}".format(name, age, height))
# ^ : 가운데 정렬, > : 오른쪽 정렬 , < : 왼쪽정렬

# =====newformat5  =====
name = "한결"
age = 16
height = 162.5
print("이름:{0:$^10s}, 나이:{1:>05d}, 키:{2:!<8.2f}".format(name, age, height))
#공간이 남으면 $로 채워라. 오른쪽 정렬하면서 0으로 채워라. 왼쪽정렬하면서 !로 채워라.

#===== 1000단위 , 사용 =====
num = 1000000
print('{:,}'.format(num))