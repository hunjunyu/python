# Ex03_json.py

f = open('./data/temp.json','rt',encoding='utf-8')
data = f.read()
f.close()

print(data)
print(type(data))

import  json
item = json.loads(data)

print(item)
print(type(item))

for k,val in item.items():
    print(k,val)
    print(k,val['Job'])

















