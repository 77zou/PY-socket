import json

# Python类型数据->json字符串：json.dumps()
json_str = '''[{"provinceName": "美国","currentConfirmedCount": 10086,"confirmedCount": 18888},
{"provinceName": "英国","currentConfirmedCount": 10000,"confirmedCount": 8888}]'''
python_data1 = json.loads(json_str)
json_str = json.dumps(python_data1,ensure_ascii=False)
print(json_str)

# Python类型数据->以json形式写入文件：with open(文件的相对/绝对路径,'w') as x;    json.dump()
with open('test1.json', 'w') as py:
    json.dump(python_data1,py,ensure_ascii=False)


