# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你两个整数a和b（-10000<a,b<10000），请你判断是否存在两个整数，他们的和为a，乘积为b。
若存在，输出Yes,否则输出No
例如：a=9,b=15, 此时不存在两个整数满足上述条件，所以应该输出No。
'''

def heji(a, b):
	b = abs(b)
	if b==0:
		# return 0, a
		return 'Yes'
	else:
		for i in range(1, int(b**0.5)+1):
			if b%i==0:
				if i+b/i==a:
					# return i, b/i
					return 'Yes'
				elif 0-i-b/i==a:
					# return -i, -b/i
					return 'Yes'
				elif b/i-i==a:
					# return -i, b/i
					return 'Yes'
				elif i-b/i==a:
					# return i, -b/i
					return 'Yes'
				else:
					continue
			else:
				continue
	return 'No'

a, b = -1, 0
print heji(a, b)
