# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 第一行告诉macos和linux这是一个python执行程序，win会忽略它
# 第二行告诉系统这使用的是utf-8编码

from collections import Iterable

L = ['micheal', 'sarah', 'Tracy', 'bob', 'jack']
print(L[0], L[1], L[2])

r = []
n = 3
for i in range(n):
    r.append(L[i])
print('hh')
print(r)

print(L[0:3])
print(L[:3])
print(L[-2:])


# 去除字符串首尾的空格
def trim(str):
    if(len(str) == 0 or (str[0]!=' ' and str[-1]!=' ')):
        return str
    elif str[0]==' ':
        return trim(str[1:])
    else:
        return trim(str[:-1])

        # print(trim(str[0] =='' and str[1:] or str[:-1]))
        # return trim(str[0] =='' and str[1:] or str[:-1])


print(trim("           1233"))
print(trim("           1233      "))


# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k,v in d.items():
    print(k, ':', v)

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if isinstance(L, list)!=True:
        return "is no a list"
    max = L[0]
    min = L[0]
    for x in L:
        if x > max:
            max = x
        if x < min:
            min = x
    return (min, max)

print(findMinAndMax([100, 2, 6, 19, 20]))


# 列表生成式