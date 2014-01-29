# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个正整数列表 L, 如 L=[2,8,3,50], 判断列表内所有数字乘积的最后一个非零数字的奇偶性,
奇数输出1,偶数输出0. 如样例输出应为0
'''

l = [2, 5, 10]
n = 1
for i in l:
    n *= i
while n%10==0:
    n = n/10
t = n%10
print t%2