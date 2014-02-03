#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
还记得中学时候学过的杨辉三角吗？具体的定义这里不再描述，你可以参考以下的图形：
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
..............
先在给你一个正整数n，请你输出杨辉三角的前n层
注意：层数从1开始计数,每层数字之间用一个空格隔开，行尾不要有空格。
如n=2,则输出：
1
1 1
'''

def yanghuisanjiao(n):
	l = [[] for i in range(n)]
	l[0].append('1')
	for i in range(1, n):
		l[i].append('1')
		for j in range(1, i):
			l[i].append(str(int(l[i-1][j-1]) + int(l[i-1][j])))
		l[i].append('1')
	return l

def printYanghuisanjiao(l):
	num = len(l)
	for item in l:
		print ' '.join(item)

printYanghuisanjiao(yanghuisanjiao(5))

			
