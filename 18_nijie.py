# -*- coding: utf-8 -*-

import sys

def sushu(num):
	l = [2]
	k=0
	for i in range(2, num+1):
	    for j in range(2, i):
	        if i%j==0:
	            break
	        k = j
	    if k==i-1:
	        l.append(i)
	return l

def fenjie(num):
	l = sushu(num)
	temp = num
	k = []
	while temp not in l:
		for i in l:
			i = int(i)
			if temp%i==0:
				temp = temp/i
				k.append(i)
				break
	k.append(temp)
	return k

def cheng(l):
	num = 1
	for i in l:
		num *= i
	return num

def zuhe(l):
	k = []
	for i,n in enumerate(l):
		l.remove(n)
		t = [n, cheng(l)]
		if t not in k:
			k.append([n, cheng(l)])
		l.insert(i, n)
	return k

def nijie(a, b):
	l = fenjie(max(a, b))
	k = fenjie(min(a, b))

	for i in k:
		l.remove(i)
	if len(l)==1:
		l.append(1)
	if len(l)==2:
		x = l[0] * min(a, b)
		y = l[1] * min(a, b)
		return [x, y]
	else:
		m = zuhe(l)
		k = []
		for t in m:
			x = t[0] * min(a, b)
			y = t[1] * min(a, b)
			k.append([x,y])
		return k

print nijie(int(sys.argv[1]), int(sys.argv[2]))

