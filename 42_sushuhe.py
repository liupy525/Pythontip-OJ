# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
把一个偶数拆成两个不同素数的和，有几种拆法呢？
现在来考虑考虑这个问题，给你一个不超过10000的正的偶数n，
计算将该数拆成两个不同的素数之和的方法数，并输出。
如n=10，可以拆成3+7，只有这一种方法，因此输出1.
'''

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
	
def  sushuhe(num):
	l = sushu(num)
	s = 0
	for i in l:
		if num-i in l:
			s += 1
	return s/2

print sushuhe(6)
