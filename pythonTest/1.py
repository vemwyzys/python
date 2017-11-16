# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 第一行告诉macos和linux这是一个python执行程序，win会忽略它
# 第二行告诉系统这使用的是utf-8编码
print(100+200+500/3)
print('the sabi is saying the','big lie','haha')
print('100+200+300=',100+200+300)
# name = input('please input your name : ')
# print('hello',name)

print('1024 * 768 = ',1024*768)
print('I\'m sabi')
print('I\n \'m sabi')
print('I\\ \'m sabi')
print(r'''\\\\\\
...line
...line''')
print(ord('a'))
print(chr(99))
# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (s2-s1)/s1
print('%1.2f'%r)

##################################################################################
# list数组
classmates = ['michael','bob','tracy']
print(classmates)
print(classmates[0])
print(classmates[1])
# -1获取最后一个元素
print(classmates[-1])
# -2获取倒数第二个元素       角标可以正一圈,反一圈
print(classmates[-2])
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)
print(len(classmates))
# tuple元组
classmates2 = ('nick', 'mick', 'doll')
# tuple不能改变元素,获取和list一样,除非多维数(元)组,里面的list数组可以改变
# tuple的陷阱: 只有一个元素的tuple,要打逗号,不然会认为是小括号
t = (1, )

# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

####################################################################################
# 判断
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

age = 3
if age >= 18:
    print('adult')
elif age >= \
        6:
    print('teenager')
else:
    print('kid')

# input得到的是字符串,所以要强转int,才能比较
# by = input('the year of your birth : ')
# by = int(by)
# if by < 2000:
#     print('00前')
# else:
#     print('00后')

# 练习
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# 用if-elif判断并打印结果：

height = 1.75
weight = 80.5
bmi = weight/(height ** 2)
if bmi >= 32:
    print('过胖')
elif bmi >= 28:
    print('肥胖')
elif bmi >= 25:
    print('过重')
elif bmi >= 18.5:
    print('正常')
else:
    print('过轻')


#################################################################################
# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


# 从1加到100    101是一百
sum = 0
for x in range(101):
    sum = sum + x
print(sum)


Sum = 0
n = 99
while n > 0:
    Sum = Sum + n
    n = n - 2
print(Sum)


n = 1
while n < 100:
    if n >=10:
        break
    print(n)
    n = n + 1
print('END')


n = 0
while n < 100:
    n = n + 1
    if n >= 10:
        break
    elif n % 2 == 0:
        continue
    print(n)
print('END')

###########################################################################################
# dict  (dictionary)(相当于map)
d = {'Michael': 95, 'Bob': 85, 'Tracy': 54}
print(d['Michael'])
print(('nick' in d))
d['Bob'] = 17
print(d['Bob'])
# 下行如果没有,则输出none
print(d.get('nick'))
# 下行如果没有,则输出指定的数值(这里是-1)
print(d.get('nick', -1))

# set
# set只有非重复的key, 无value
# 新建set需要提供一个list,且会把里面重复的祛除
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)


a = ['c', 'b', 'a']
a.sort()
print(a)

t = (1, 2, 3)
d = {t, }
print(d)
s = set(t)
print(s)

d = {s, }
print('hh')
print(d)


t1 = (1, [2, 4])
# t这个tople中有list,list是可变的,所以放不进dict中(因 unhashable)
# d = {t1, }
# print(d)
#
# set初始化的时候需要一个list传入值, 但是元组内有list不行,
# set初始化可list传入可能是一种官方的便捷方法而已,实际set内部放入的是list经过转化后的值(哈希,无序,不重复)
# set本身是无须排列的可哈希的值,  不可放入dict
# s1 = set(t1)
# print('hh')
# print(s1)
# print('hh')
