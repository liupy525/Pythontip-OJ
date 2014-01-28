# -*- coding: utf-8 -*-

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
	
print sushu(8)