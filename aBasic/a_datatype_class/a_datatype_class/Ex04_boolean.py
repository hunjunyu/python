# 부울형 - 첫글자는 반드시 대문자 True, False, None 여야 한다
t = True
f = False
n = None    # 다른 언어의  null 값과 유사

hungry =  True
sleepy = False

print(not hungry)
print(hungry and sleepy)
print(hungry or sleepy )
print(hungry & sleepy)
print(hungry | sleepy )




"""
        자료형         값           부울형
    -----------------------------------------------------
        문자형       "문자"          True
                    ""                     False
        리스트       [1,2,3]         True       
                    []                     False
        튜플         ()                     False
        딕셔너리     {}                     False
        숫자형       0이아닌 숫자     True
                    0                      False
                    None                   False
"""
print('========================================')
if '아':
    print('True') #true
else:
    print('False')

if []:#false
    print('True2')
else:
    print('False2')

if 0:#false
    print('True3')
else:
    print('False3')

msg = '행복합시다'
if msg.find('행'):
    print('ok')
else:
    print('no')

if msg.find('가')>-1:
    print('ok')
else:
    print('no')