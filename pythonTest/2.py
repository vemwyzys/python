# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 第一行告诉macos和linux这是一个python执行程序，win会忽略它
# 第二行告诉系统这使用的是utf-8编码
import math

PI = 3.14
# abs()返回绝对值
print(abs(3.14))
print(str('123'))
print(int(16.98))
print(bool(''))
print(hex(2))


def my_ass(x):
    if x >= 0:
        return x
    else:
        return -x


# x = int(input("输入数字"))
# print(my_ass(x))


def nop():
    pass


age = 20
if age >= 18:
    pass


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# i = 'abc'
# print(my_abs(i))


def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# Python的函数返回多值其实就是返回一个tuple，但写起来更方便
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
print(math.sqrt(2))


def quadratic(a, b, c):
    if a == 0:
        x1 = -(c / b)
        x2 = x1
        return x1, x2
    else:
        delta = b**2 - 4*a*c
        if delta == 0:
            x1 = -(b/(2*a))
            x2 = x1
            return x1, x2
        elif delta >0:
            x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
            x2 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
            return x1, x2
        else:
            return '实数域内无解,在虚数域内有两个实根'


print('第一例')
print(quadratic(1, 2, 3))
print('第二例')
print(quadratic(6, 6, 0))
print('第3例')
print(quadratic(0, 6, 6))


# 计算次方,默认次幂为2
def power(b, n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*b
    return s


print(power(3))


def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)


print(enroll('wss', '3'))


def enroll(name, gender, age=6, city='hangzhou'):
    print('name: ', name)
    print('gender: ', gender)
    print('age: ', age)
    print('city: ', city)


print(enroll('wangsongsong', '6', '13', 'huainan'))


def add_end(L=[]):
    L.append('End')
    return L


print(add_end([1, 2, 3]))


def add_end(L=None):
    if L is None:
        L = []
    L.append('end')
    return L


print(add_end())


# 计算a平方+b平方+...................
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n *n
    return sum


# 调用上边的calc函数时, 需要预先组装一个list或tuple
print(calc([1, 2, 3]))


# 如果利用可变参数, 调用函数可以简化成calc(1, 2, 3)

# 下面我们把函数的参数改为可变参数   加*后numbers内部接受到的是一个tuple,可以传入任意个参数,0个都可以
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum +n *n
    return sum


print(calc(1, 2, 3))


# 如果已经有了一个list或者tuple, 要调用一个可变参数怎么办?
# 可以如下  但是很麻烦
nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))


# 如上是可行的, 问题是太繁琐,所以Python允许你再list或tuple前面加一个*号, 把list或tuple的元素变成可变参数传入函数
nums = [1, 2, 3]
print(calc(*nums))
# 如上 *nums表示把nums这个list的所有元素作为可变参数传入进入, 很常见很好用


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name: ', name, 'age: ', age, 'other: ', kw)


print(person('jack', 27, city='beijing', job='socker', ad='hang'))

# 其上 kw可以不传入
print(person('wss', 25))

# kw也可以传入任意个关键字参数
print(person('bob', 35, city='hangzhou', job='engineer'))
# 利用**kw这个关键字参数可以扩展这个calc函数,多接收几个参数(可选)

# 和可变参数类似, 也可以先事先组装一个dict, 然后, 把该dict转换为关键字参数传进去
extra = {'city': 'guangzhou', 'job': 'whole'}
print(person('nick', 48, city=extra['city'], job=extra['job']))
# 上一句很麻烦, 可以这样写
print(person('bitch', 23, **extra))

# 总结:**extra的意思是把这个字典的所有key-value用关键字参数传入函数中**kw参数中
# kw将获得一个字典, 注意这是获得一个复制而已


# 命名关键字参数(因为上面的**kw不限制传入的参数,现在需要限制)
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。


print(person('jack', 27, city='beijing', job='socker'))


# *args是可变参数, 可变参数后面的参数会成为关键字参数(关键字参数需要参数名, 如:city='hangzhou')
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


print(person('jack', 27, 1, 2, 3, city='beijing', job='socker'))
# print(person('jack', 27, 1, 2, 4, 'beijing', 'socker'))


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('位置参数a =', a, '位置参数b =', b,
          '默认参数c =', c,
          '可变参数args=', args,
          '关键字参数kw=', kw)


print(f1(1, 2))


# 计算多个数的乘积
def product(*nums):
    if nums is None or len(nums) <= 0:
        return "无参数"
    product = 1
    for num in nums:
        product = product * num
    return product


print(product(3, 9))
print(product())


# 递归函数
def fact(n):
    if n ==1:
        return 1
    return n*fact(n - 1)


print(fact(3))


def pickupliyu(depth):
    print("抱着")
    if depth == 0:
        print("我的小鲤鱼")
    else:
        pickupliyu(depth - 1)
    print("的我")


print("吓得我抱起了 ")
pickupliyu(4)

L = []
n = 1
while n <= 19:
    L.append(n)
    n = n + 2
print(L)