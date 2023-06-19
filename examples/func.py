# 返回多个值
def my_func(x, y):
    new_x = x + 1
    new_y = x + y
    return new_x, new_y  # 实则为省略了 () 的元组


x, y = my_func(1, 2)
print(x)  # 2
print(y)  # 3


# 默认值的坑，默认值不是惰性的，在函数定义时就被创建了
def add_end(list=[]):
    list.append(1)
    return list


# 解法
# def add_end(list = None):
#   if list is None:
#     list = []

#   list.append(1)
#   return list

print(add_end())  # [1]
print(add_end())  # [1, 1]
print(add_end())  # [1, 1, 1]

result = add_end()
print(result)  # [1, 1, 1, 1]
result.append(2)
print(result)  # [1, 1, 1, 1, 2]
print(add_end())  # [1, 1, 1, 1, 2, 1]


# 解法就是
def add_end(list=None):
    if list is None:
        list = []

    list.append(1)
    return list


# 参数位置
