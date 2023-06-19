# TODO: why?
print('10' == 10)

age = 18
if age >= 18:
    print('成年人')
elif age > 6:
    print('青少年')
else:
    print('儿童')


t = []
if t:  # 非零整数、非空字符串、非空 list 就为 true
    print('t 不为空')
else:
    print('t 为空')
