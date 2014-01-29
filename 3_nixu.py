# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个字符串 a， 如a=‘12345’，对a进行逆序输出a。
'''

def nixu(s):
    l = list(s)
    l.reverse() # or [::-1]
    return ''.join(l)

print nixu('nihao')

