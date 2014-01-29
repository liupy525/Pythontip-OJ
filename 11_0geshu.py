# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个正整数列表 L, 如 L=[2,8,3,50], 输出L内所有数字的乘积末尾0的个数,
如样例L的结果为2.(提示:不要直接相乘,数字很多,可能溢出)
'''
l = [2, 5, 10]
n = 1
for i in l:
    n *= i
t = 0
while n%10==0:
    t += 1
    n /= 10

print t