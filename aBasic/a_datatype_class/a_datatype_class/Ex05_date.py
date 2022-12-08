'''
import datetime
today = datetime.date.today()
print('today is ', today)

from datetime import date,timedelta
today = date.today()
print('today is ', today)

from datetime import date ,timedelta
print('년도 : ', today.year)
print('월 : ', today.month)
print('일 : ', today.day)
print('요일 : ', today.weekday())

print('어제 : ',today+timedelta(days=-1))
print('7일전 : ',today+timedelta(days=-7))
print('10일후 : ',today+timedelta(days=+10))

from datetime import datetime
day = datetime.today()
print(day)
'''
import datetime
day = datetime.datetime.today()
print(day.strftime('%Y년 %m월 %d일 %H:%M'))

iiinal = '2022-12-25 12:50:59'

print(type(iiinal))
mydate = datetime.datetime.strptime(iiinal,'%Y-%m-%d %H:%M:%S')
print(mydate)
# 날짜를 문자열 형태 (strftime() 이용)
# 문자열을 날짜형태 ( strptime() 이용)


