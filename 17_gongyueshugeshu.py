# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你两个正整数a,b,  输出它们公约数的个数。
'''

def yueshu(num):
	l = []
	for i in range(1, num+1):
		if num%i==0:
			l.append(i)
	return l

def numOfGongyueshu(a, b):
	num = 0
	l = yueshu(a)
	k = yueshu(b)

	for i in l:
		if i in k:
			num += 1

	return num

print numOfGongyueshu(12, 24)
