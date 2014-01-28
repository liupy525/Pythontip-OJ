#!/usr/bin/env python
# -*- coding: utf-8 -*-

def xunhuanxiaoshu(a, b):
	l = []
	xunhuan = ['%d' %(a/b), '.']
	dindex = xunhuan.index('.')
	index = 0
	a = a%b
	while True:
		t, a  = divmod(a*10, b)
		temp = (t, a)
		if temp not in l:
			l.append(temp)
			xunhuan.append(str(t))
		else:
			index = l.index(temp)
			break
	return (xunhuan[:dindex+index+1], xunhuan[dindex+index+1:])
	# return ''.join([''.join(xunhuan[:dindex+index+1]), '(', ''.join(xunhuan[dindex+index+1:]), ')'])

# print xunhuanxiaoshu(1231, 65)
print xunhuanxiaoshu(1, 2)
