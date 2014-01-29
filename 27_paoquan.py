# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
一个环形的公路上有n个加油站，编号为0,1,2,...n-1,
每个加油站加油都有一个上限，保存在列表limit中，即limit[i]为第i个加油站加油的上限，
而从第i个加油站开车开到第(i+1)%n个加油站需要cost[i]升油,cost为一个列表。
现在有一辆开始时没有油的车，要从一个加油站出发绕这个公路跑一圈回到起点。
给你整数n，列表limit和列表cost,你来判断能否完成任务。
如果能够完成任务，输出起始的加油站编号，如果有多个,输出编号最小的。
如果不能完成任务，输出-1。
'''

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
