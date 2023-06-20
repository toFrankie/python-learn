# 基础

## 输入与输出

```py
# 输入
print('something')
print(expression)

# 输出
variable = input()
```

## 注释

```py
# some comments
other statements
```

## 语法

Python 语法采用缩进的方式，但没有规定缩进是几个 Space 还是 Tab。按照约定俗成的惯例，应该始终坚持使用 4 个空格的缩进。当语句以冒号 `:` 结尾时，缩进的语句视为代码块。

## 数据类型

- 整数
- 浮点数
- 字符串
- 布尔值（`True`、`False`，注意大小写）
- 空值（用 `None` 表示，类似 JavaScript 中的 `null`）
- 列表
  - 数组
  - 元组（tuple），不可变的有序列表，形式如 `t = (1, 2)`。
- 字典（dict，键值对形式）
  - dict：键值对形式，类似 JavaScript 中的 Object。
  - set：只存放 key，没有 value，是一种无序、无重复元素的集合。
- 允许自定义数据类型？

> 其中特殊值 `None` 表示空值或者缺省值。相当于 JavaScript 中的 `undefined`。

注意点：

- 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（包括除法），而浮点数运算则可能会有四舍五入的误差（关于前者的说法有保留，在 Python 中除法有 `/` 和 `//` 两种）。
- 对于字符串，可通过 `r''` 表示内部默认不转义。
- 如果字符串内部有很多换行，用 `\n` 写在一行里不好阅读，可用 `'''some text...'''` 的格式表示多行内容。
- JavaScript 中的 `&&`、`||`、`!`，在 Python 中用 `and`、`or`、`not` 表示。比如：`not 1 > 2` 结果为 `True`。
- 可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量。与 JavaScript 类似，是动态语言。
- 在 Python 中没有 `===` 全等比较，而 `==` 与 JavaScript 类似，也会尝试转换类型。若要全等比较，可以用 `is`，会检查类型、地址和值。
- 在 JavaScript 中获取数组、字符串长度时，是采用 `xxx.length` 形式，而 Python 中使用 `len()` 方法获取。
- 对于数组类型，若索引超出范围，会抛出 IndexError。
- 对于元组类型，若是空元组，用 `t = ()` 表示；若只有一项，需表示为 `t = (1,)`，而 `t = (1)` 会被认为是表达式，变量 `t` 是一个整数类型。
- 对于元组类型的「不可变」，指的是每项元素指向不变。比如元组中某项是一个数组，其实是可以修改数组某个值的，因为数组指向没有发生改变。
- 对于字典类型，比如：`person = {'name': 'Frankie'}`，与 JavaScript 的区别有这些：键的引号不能缺省，没有 `person.name` 语法获取某个键值，只能通过 `person['name']` 或 `person.get('name')` 形式获取。
  - 对于 `person['name']` 形式，若 key 不存在，会抛出 KeyError。
  - 对于 `person.get('name')` 形式，若 key 不存在，会返回 `None`。

待解决：

- 相等比较 `==` 以及 `is` 操作符的细节，为什么 `print('10' == 10)` 结果为 `False`。

### 四种数据类型对比

在 Python 中，`list`、`tuple`、`dict` 和 `set` 是四种常见的数据类型，它们各自有不同的特点和用途：

**list**（列表）：

- 特点：有序、可变（mutable）的序列，可以包含任意类型的元素，并且允许重复元素。
- 用途：常用于存储和处理多个相关的值，可以进行增加、删除、修改和访问元素等操作。
- 示例：

```py
numbers = [1, 2, 3, 4, 5]  # 整数列表
names = ['Alice', 'Bob', 'Charlie']  # 字符串列表
```

**tuple**（元组）：

- 特点：有序、不可变（immutable）的序列，可以包含任意类型的元素，并且允许重复元素。
- 用途：常用于存储不可变的数据，如函数返回多个值、字典中的键值对等。
- 示例：

```py
coordinates = (10, 20)  # 坐标元组
person = ('Alice', 25, 'New York')  # 个人信息元组
```

**dict**（字典）：

- 特点：无序的键值对集合，每个键都是唯一的，键和值可以是任意类型的对象。
- 用途：用于存储和查找具有关联关系的数据，键用于唯一标识和访问值。
- 示例：

```py
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}  # 个人信息字典
student = {'id': 123, 'name': 'Bob', 'courses': ['Math', 'Science']}  # 学生信息字典
```

**set**（集合）：

- 特点：无序、可变的元素集合，每个元素都是唯一的，不能包含重复元素。
- 用途：用于存储和操作不重复的数据集合，可以进行集合运算（如交集、并集、差集）等操作。
- 示例：

```py
fruits = {'apple', 'banana', 'orange'}  # 水果集合
primes = {2, 3, 5, 7, 11}  # 素数集合
```

## 类型转换

```py
int(x)  # 转换成整数
float(x)  # 转换成浮点数
str(x)  # 转换成字符串
bool(x)  # 转换成布尔值
```

类似 JavaScript 中的 `String()`、`Boolean()` 等方法。

## 条件判断

语法如下：

```py
age = 18

if age >= 18:
    print('成年人')
elif age > 6:
    print('青少年')
else:
    print('儿童')
```

> 注意，条件后面的冒号 `:` 不能省略，后面缩进表示代码块。

对于三目运算，Python 中没有类似 JavaScript 中 `const x = condition ? true_value : false_value` 三目运算形式。而是采用 `if` 表达式来表示三目运算，如下：

```py
x = true_value if condition else false_value
```

注意点：

- 判断条件可简写，比如：`if x:` 只要 `x` 是非零数值（包括整数和浮点数）、非空字符串、非空列表等，就判断为 `True`，否则为 `False`。这点与 JavaScript 是有区别的。

## 循环

- `for...in` 用于遍历可迭代对象。
- `while`

```py
# for
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# while
count = 0
while count < 5:
    print(count)
    count += 1

# 快速创建新数组
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)  # 输出: [1, 4, 9, 16, 25]
```

`break` 和 `continue` 跟 JavaScript 一致。
