# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 请定义一个函数quadratic(a, b, c), 接受3个参数,返回一元二次方程的解(带有代数):
# 范例: ax^2 + bx + c = 0 (a!=0)的两个解
import math


def quadratic(a, b, c):
    for i in a, b, c:
        if not isinstance(i, (int, float)):
            raise TypeError('int or float')

    if a ==0:
        raise SyntaxError("error! a !=0")

    d = b**2 - 4*a*c
    if d <= 0:
        return print('error')
    elif d >= 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b + math.sqrt(d)) / (2*a)
        return x1, x2


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))