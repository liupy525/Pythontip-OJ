# -*- coding: utf-8 -*-

def howManyMountains(h):
	num = 0
	for i in range(1, len(h)-1):
		if h[i]>h[i-1] and h[i]>h[i+1]:
			num += 1
	return num

h = [0.9,1.2,1.22,1.1,1.6,0.99]
print howManyMountains(h)
