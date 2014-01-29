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
	return xunhuan[:dindex+index+1], xunhuan[dindex+index+1:]

def createPwd(a, b, x, y):
	l, k = xunhuanxiaoshu(a, b)
	l = l[l.index('.')+1 : ]
	m = len(l)
	n = len(k)

	delta = y-x+1
	pwd = []
	t1 = t2 = 0

	if x<=m:
		if delta<(m-x+1):
			pwd.extend(l[x-1:x+delta-1])
			print 'a'
			return pwd			
		print 'b'
		pwd.extend(l[x-1:])
		t1, t2 = divmod(delta-(m-x+1), n)
		for i in range(t1):
			pwd.extend(k)
		pwd.extend(k[:t2])
	else:
		x = (x-m)%n
		if delta<(n-x+1):
			print 'c'
			pwd.extend(k[x-1:x+delta-1])
			return ''.join(pwd)
		print 'd'
		pwd.extend(k[x-1:])
		t1, t2 = divmod(delta-(n-x+1), n)
		for i in range(t1):
			pwd.extend(k)
		pwd.extend(k[:t2+1])
	return ''.join(pwd)

a=1
b=2
x=1
y=5
print createPwd(a, b, x, y)
