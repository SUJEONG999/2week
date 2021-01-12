print('{} and {}'.format('You', 'Me'))
print('{0} and {1} and {0}'.format('You', 'Me'))
print('{var1} are {var2}'.format(var1='You', var2='Niceman'))

print('%s: %d' % ('나이', 30))                   	 #문자열과 정수 출력
print('{}: {}'.format('나이', 30))                            # %[-]폭[.유효자리수]서식

print('%f,%.2f' % (1.123, 1.123))        		 #실수 출력
print('{:f}, {:.2f}'.format(1.123, 1.123))

print('%o, %x, %X' % (10, 10, 10))      		 #진법 출력(8진수,16진수)
print('{:b}, {:o}'.format(10, 10))  # 2진수, 8진수
print('{:x}, {:X}'.format(10, 10))  # 16진수 , 10~15은  'a'~'f'로 표시, 10~15은  'A'~'F'로 표시

print('|%5d|' % 123)      			 #고정 길이 출력
print('|%5s|' % 'abc')
print('|{:5}|'.format(123))
print('|{:5}|'.format('abc'))

print('|%-5d|' % 123)    			 # 고정 길이의 정렬
print('|%5s|' % 'abc')
print('|{:<5}|'.format(123))  # 왼쪽 정렬
print('|{:>5}|'.format('abc')) # 오른쪽 정렬
print('|{:^5}|'.format('abc')) # 가운데 정렬

print('|%05d|' % 123)           #여백 채우기, 0으로 폭 5를 채워라
print('|{:05}|'.format(123))
print('|{:_>5}|'.format('abc'))  # _으로 폭 5를 채우고 오른쪽 정렬
print('|{:-^5}|'.format('abc'))

print('{:,}'.format(1000000))        		#정수, 실수 단위 구분
print('{:,.2f}'.format(1000000))
