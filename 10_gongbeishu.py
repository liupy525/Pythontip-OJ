# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你两个正整数a和b， 输出它们的最小公倍数
'''

def gongyueshu(a, b):
    n = 1
    for i in range (2, min(a,b)+1):
        if a%i==0 and b%i==0:
            n = i
    return n

def gongbeishu(a, b):
    return a*b/gongyueshu(a, b)

print gongbeishu(12, 39)