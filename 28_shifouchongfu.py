# -*- coding:utf-8 -*-

def isChongfu(L):
	if sorted(L)==sorted(list(set(L))):
		return False
	else:
		print True

L = [56,25,12,657786,2,34,23,65,43,3,53]
if isChongfu(L):
	print "YES"
else:
	print "NO"
