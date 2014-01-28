# -*- coding: utf-8 -*-

def huiwen(a, n):
	l = list(a)
	for i in range(0, len(l)-n+1):
		k = l[i:i+n]
		m = l[i:i+n]
		m.reverse()
		if m==k:
			return True
	return False

print huiwen('1234355', 3)