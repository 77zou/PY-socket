import json
# json字符串->Python类型数据：json.loads(json字符串)
json_str = '''[{"provinceName": "美国","currentConfirmedCount": 10086,"confirmedCount": 18888},
{"provinceName": "英国","currentConfirmedCount": 10000,"confirmedCount": 8888}]'''
python_data1 = json.loads(json_str)
print(python_data1)
print(type(python_data1))
print(type(json_str))

# json格式的文件对象->Python类型数据：json.load(文件的相对/绝对路径)
with open('test.json') as js:
    python_data2 = json.load(js)
    print(python_data2)
    print(type(python_data2))
    print(type(python_data2[0]))