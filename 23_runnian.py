# -*- coding: utf-8 -*-

def isRunnian(year):
	if year%100==0:
		if year%400==0:
			return True
		else:
			return False
	elif year%4==0:
		return True
	else:
		return False

print isRunnian(2100)
