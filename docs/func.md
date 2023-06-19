# 函数

在 Python 中内置了很多函数，可以在 [Built-in Functions](https://docs.python.org/3/library/functions.html#built-in-functions) 中查看。

- 函数参数分为必选参数、可选参数（表示设置了参数默认值），在调用函数时要注意传参数量：一是不能超过函数参数总数，二是不小于必选参数的数量，否则会抛出 TypeError。其中 `min()` 和 `max()` 可以接收任意多个参数。
- 在 Python 中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这 5 种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

## 函数定义

在 Python 中，使用 `def` 关键字定义函数：

```py
def my_func(x):
  if x > 18:
    return True
  else:
    return False
```

如果没有 `return` 语句，函数执行完毕后也会返回结果，只是结果为 `None`。`return None` 可以简写为 `return`。

#### 返回多个值

```py
def my_func(x, y):
  new_x = x + 1
  new_y = x + y
  return new_x, new_y


x, y = my_func(1, 2)
print(x) # 2
print(y) # 3
```

其实这是一个假象，上述函数只是返回了一个元组（tuple），而多个变量可以接受一个 tuple，只要位置对应即可。类似 JavaScript 中返回一个数组，然后对数组解构，然后省略数组两边的 `[` 和 `]`。

#### 参数默认值

```py
def greet(name=None):
    if name is None:
        print("Hello, stranger!")
    else:
        print(f"Hello, {name}!")

greet()  # 输出: Hello, stranger!
greet("Alice")  # 输出: Hello, Alice!
```

关于参数默认值有一个「坑」：

```py
def add_end(list = []):
  list.append(1)
  return list

print(add_end()) # [1]
print(add_end()) # [1, 1]
```

原因是：在函数在定义时，list 就被创建了，函数每次调用，这个默认值都是指向了内存中的同一个地址。而在 JavaScript 中，函数参数默认值是惰性的，所以每次调用函数当参数缺省时，它才会去创建，同样的函数就不会出现上面的问题。

解法是：

```py
def add_end(list = None):
  if list is None:
    list = []

  list.append(1)
  return list
```

> **因此，函数参数默认值应设为不可变对象**。

#### 可变参数

前面提到，函数定义或者调用参数数量要对应上。那么对应像 min()、max() 等数量不定的函数来说，要怎么实现呢？

一是利用 list 和 tuple：

```py
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 传入数组
calc([1, 2, 3]) # 14

# 传入元组
calc([1, 3, 5, 7]) # 84
```

利用可变数组的话

```py
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2, 3) # 14
calc(1, 3, 5, 7) # 84
```

区别在于，可变参数的前面加了一个 `*`，这样的话，函数内部 `number` 将接收到一个元组。但函数调用时，可以指定不同数量的参数，甚至是 `0` 个。

如果入参值本身就是一个 list 或 tuple 呢，可以这样 `calc(*[1, 2])`。

没错，像极了 JavaScript 中的 Rest Parameters 和 Spread Syntax。

#### 关键字参数

```py
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing') # name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer') # name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```

作用就是把一些非必要的参数组成一个 dict。

#### 命名关键字参数

对于前面关键字参数，如果我们希望检查 `city` 和 `job` 参数，可以利用 `in` 关键字处理：

```py
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
```

但如果我们要限制 `kw` 里最多只有 `city` 和 `job`，可以使用命名关键字参数：

```py
def person(name, age, *, city, job):
    print(name, age, city, job)
```

命名关键字参数需要一个特殊分隔符 `*`，`*` 后面的参数被视为命名关键字参数。

#### 空函数

如果想定义一个什么事也不做的空函数，可以用 `pass` 语句：

```py
def noop():
  paas
```

#### 异常处理

TODO

#### 参数类型检查

可借助内置函数 `isinstance()` 处理：

```py
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
```
