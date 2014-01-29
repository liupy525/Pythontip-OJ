# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个字符串列表L，请用一行代码将列表所有元素拼接成一个字符串并输出。
如L=['abc','d','efg'], 则输出abcdefg。
'''

def zhuanhuan(l):
	return ''.join(l)

L = ['abc','d','efg']
print zhuanhuan(L)
