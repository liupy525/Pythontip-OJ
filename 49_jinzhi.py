#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个十进制数a，将它转换成b进制数,如果b>10,用大写字母表示（10用A表示，等等）
a为32位整数，2 <= b <= 16
如a=3,b = 2, 则输出11
'''

def jinzhi(num, x):
	if num<0:  # 千万不要忘记num为负的情况
		flag = True
		num = -num
	else:
		flag = False
	temp = num
	l = []
	while temp:
		t = temp%x
		if t>9:
			l.append(chr(ord(str(t-10))+17))
		else:
			l.append(str(t))
		temp = temp / x
	l.reverse()
	if flag:
		l.insert(0, '-')
	return ''.join(l)

a, b = -14, 16
print jinzhi(a, b)
