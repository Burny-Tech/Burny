# python 数据 和json数据相互转换

"""
转为json
json.dumps(data,ensure_ascii=False)
json转为要的数据本身可以拥有的格式
json.loads(json_str)
"""
import  json

data = [{"age":"s"},{"f":"s"}]
# true 或者不填：中文会变成asici码
json_str = json.dumps(data,ensure_ascii=False)

print(type(json_str))
print(json_str)

list_str = json.loads(json_str)

print(type(list_str))
print(list_str)



"""
<class 'str'>
[{"age": "s"}, {"f": "s"}]
<class 'list'>
[{'age': 's'}, {'f': 's'}]
"""