# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你三个整数a,b,c,  判断能否以它们为三个边长构成三角形。
若能，输出YES，否则输出NO。
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

a=3
b=4
c=5

if isTriangle(a, b, c):
	print "YES"
else:
	print "NO"

