# -*- coding: utf-8 -*-

def isYouxu(l):
	k = sorted(l)
	m = sorted(l, reverse=True)
	if k==l:
		return 'UP'
	elif m==l:
		return 'DOWN'
	else:
		return 'WRONG'

print isYouxu([4,3,2])
