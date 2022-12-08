"""
    [ dictionary 형 ]

    1- 키와 값으로 구성 ( 자바의 map 와 유사 )
    2- 저장된 자료의 순서는 의미 없음
    3- 중괄호 {} 사용
    4- 변경가능

    ` 사전.keys() : key만 추출 (임의의 순서)
    ` 사전.values() : value만 추출 (임의의 순서)
    ` 사전.items() : key와 value를 튜플로 추출 (임의의 순서)
"""

print('--------- 1. 딕셔너리 요소 --------------- ')
dt = {1:'one', 2:'two', '3':'three'}
print(dt)
print(dt[1])
print(dt['3'])


# 키는 숫자와 문자 그리고 튜플이여야 한다. 즉 리스트는 안된다.
# 리스트의  값이 변경 가능하다. 그러나 키값을 변경하면 안되므로 리스트는 안된다
dt2 = {1:'one', 2:'two', (3,4):'turple'}
print(dt2[(3,4)])
dt2[(3,4)] = 'pyton'
print(dt2)



print('--------- 2. 딕셔너리 추가 및 수정  --------------- ')
# 딕셔너리에 값 추가 및 수정
dt2['korea'] = 'seoul'
print(dt2)
dt2['korea']  = '한국'
print(dt2)

# 여러개 추가할 때


print('--------- 3. Key로 Value값 찾기  --------------- ')

print(dt2.keys())
print(dt2.values())
print(dt2.items())

dict_1 = {2:1, 4:2, 6:3, 8:4, 10:6}
dict_keys = list(dict_1.keys())
print(dict_keys)
dict_values = list(dict_1.values())
dict_2 = dict()
for i in range(len(dict_keys)):
	dict_2[dict_values[i]] = dict_keys[i]

print(dict_2[2])

Mydict = {'1' : 1, '2' : 2}
Copy = Mydict
Mydict['1'] = 5
result= Mydict['1'] + Copy['1']
print(result)

a = list(range(10))
a.append(a[3])
a.pop(a[3])
a.insert(3, a[-1])
a.pop( )
print(a)


print('====================')
data_1 = {'one' : (1,2,3,4,5,6), 'two' : [1,2,3,4,5,6], 'three' : {'four' : 4, 'five' : 5}}
for k in ['one','two','three']:
	try:
		print(data_1[k][:1])
	except TypeError:
		print("error")

for k in ['one', 'two','three']:
	try:
		data_1[k][-1] = "a"
		print(data_1[k][-1])
	except TypeError :
		print("error")






# Key와 Value만 따로 검색
