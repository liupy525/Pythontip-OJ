# -*- coding: utf-8 -*-

def isTriangle(a, b, c):
	if a+b>c:
		if a+c>b:
			if b+c>a:
				return True
			else:
				return False
		else:
			return False
	else:
		return False

a=3
b=4
c=5

if isTriangle(a, b, c):
	print "YES"
else:
	print "NO"

