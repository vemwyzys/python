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

