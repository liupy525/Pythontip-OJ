# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
有一楼梯共n级，刚开始时你在第一级，若每次只能跨上一级或二级，要走上第n级，共有多少种走法？ 
现在给你一个正整数n（0<n<40),请你输出不同的走法数。
如n=2,则输出1（你只有一种走法，走一步，从第一级到第二级）
'''

def zoufa(n):
	a, b = 1, 1
	for i in range(n-2):
		a, b = b, a+b
	return b

print zoufa(3)
