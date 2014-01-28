# -*- coding: utf-8 -*-

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
