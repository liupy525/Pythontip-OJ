# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。
'''

def jisuan(x, y):
	m = max(x, y)
	n = min(x, y)
	num = 0
	if m>4:
		if n==1:
			m -= 2
			n += 1
		else:
			m -= 2
			n -= 1
		num += 1+jibu(m, n)
	elif (m==3 and n==2):
		num += 1
	elif (m==4 and (n==4 or n==2)) or (m==3 and n==1):
		num += 2
	elif (m==4 and n==3):
		num += 3
	elif (m==3 and n==3):
		num += 4
	elif (m==4 and n==1):
		num += 5
	else:
		num = -1
	return num

def jibu(x, y):
	m = max(x, y)
	n = min(x, y)
	if n>=3:
		return jisuan(m, n)
	else:
		if m%2==0:
			return -1
		else:
			if ((m-1)/2)%2+n==2:
				return -1
			else:
				return (m-1)/2



print jibu(5, 4)

