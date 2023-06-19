# dict

person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# name = person.name  # AttributeError: 'dict' object has no attribute 'name'

name = person['name']
print(name)  # 输出: Alice

# other = person['other']
# print(other)  # KeyError: 'other'

age = person.get('age')
print(age)  # 输出: 25

phone = person.get('phone')
print(phone)  # 返回 None（若是交互式命令行，则不显示 None）


# 判断 key 是否存在
if 'name' in person: # 返回 True or False
    print('name is in person')
else:
    print('name is not in person')

# 重复键后者会覆盖前者
person2 = {'name': 'Frankie', 'name': 'Mandy'}
print(person2.get('name'))  # 返回 Mandy