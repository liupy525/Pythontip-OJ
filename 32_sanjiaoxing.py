#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给以一个三角形的三边长a,b和c(边长是浮点数),请你判断三角形的形状。
若是锐角三角形，输出R,
若是直角三角形，输出Z，
若是钝角三角形，输出D，
若三边长不能构成三角形，输出W.
'''

def isTriangle(a, b, c):
	if a+b>c:
		if a+c>b:
			if b+c>a:
				return True
			else:
				return False
		else:
			return False
	else:
		return False

def triangle(a, b, c):

	if isTriangle(a, b, c):
		x = max(a, b, c)**2
		z = min(a, b, c)**2
		y = (a+b+c-max(a,b,c)-min(a,b,c))**2

		temp = y + z

		if x==temp:
			return 'Z'
		elif x<temp:
			return 'R'
		else:
			return 'D'
	else:
		return 'W'

a = 3
b = 4
c = 5

print triangle(a, b, c)
