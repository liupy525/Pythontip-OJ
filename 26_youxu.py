# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个整数组成的列表L，按照下列条件输出：
若L是升序排列的,则输出"UP";
若L是降序排列的,则输出"DOWN";
若L无序，则输出"WRONG"。
'''

def isYouxu(l):
	k = sorted(l)
	m = sorted(l, reverse=True)
	if k==l:
		return 'UP'
	elif m==l:
		return 'DOWN'
	else:
		return 'WRONG'

print isYouxu([4,3,2])
