# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个整数列表L,判断L中是否存在相同的数字，
若存在，输出YES，否则输出NO。
'''

def isChongfu(L):
	if sorted(L)==sorted(list(set(L))):
		return False
	else:
		print True

L = [56,25,12,657786,2,34,23,65,43,3,53]
if isChongfu(L):
	print "YES"
else:
	print "NO"
