# -*- coding: utf-8 -*-

def jiami(s, d):
	l = list(s)
	k = []
	for i in l:
		asc = ord(i) + d
		if asc>122:
			asc = asc-122+96
		k.append(chr(asc))
	return k

print jiami('abc', 1)
