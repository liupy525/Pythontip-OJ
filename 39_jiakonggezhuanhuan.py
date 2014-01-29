# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个字符串列表L，用一行代码顺序输出L中的元素，元素之间以一个空格隔开，注意行尾不要有空格，输出单独占一行。
如L=['abc','d','efg'], 则输出abc d efg。
'''

def zhuanhuan(l):
	return ' '.join(l)

L = ['abc','d','efg']
print zhuanhuan(L)
