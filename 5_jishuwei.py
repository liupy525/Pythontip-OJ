# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个字符串 a， 输出字符奇数位置的字符串。如a=‘12345’，则输出135。
'''

str1=''
for i in range(len(a)):
    if i%2==0:
        str1 += str(a[i])
print str1