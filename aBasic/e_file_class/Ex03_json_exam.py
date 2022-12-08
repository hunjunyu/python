#Ex03_json_exam.py

'''
data / sample.json 파일을 읽고 출력하시요

'''

with open('./data/sample.json','rt',encoding='utf-8')as f:
    data = f.read()


import json
i = json.loads(data)
print(i)
print(type(i))
co = 0
for k,val in i.items():
    co += val['price']* val['count']

print(co)


