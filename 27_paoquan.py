# -*- coding: utf-8 -*-

def nengfoupaoquan(n, limit, cost):
	start = []
	for i in range(n):
		oil = 0
		ok = True
		for j in range(n):
			m = (i+j)%n
			oil += limit[m]
			oil -= cost[m]
			if oil<0:
				ok = False
				break
		if ok:
			start.append(i)
	if start==[]:
		return -1
	else:
		return min(start)

n = 5
limit = [4,3,3,3,3]
cost = [5,3,2,3,3]

print nengfoupaoquan(n, limit, cost)
