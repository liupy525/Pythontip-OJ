# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你直角三角形的两个直角边的边长a,b,请你求出其斜边边长，结果保留小数点后三位小数。
如a=3, b =4, 则输出5.000。
'''

def xiebian(a, b):
	return '%.3f' %((a**2+b**2)**0.5)

print xiebian(3, 4)
