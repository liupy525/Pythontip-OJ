# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
十一假期,小P出去爬山,爬山的过程中每隔10米他都会记录当前点的海拔高度(以一个浮点数表示),
这些值序列保存在一个由浮点数组成的列表h中。回到家中，小P想研究一下自己经过了几个山峰，请你帮他计算一下，输出结果。
例如：h=[0.9,1.2,1.22,1.1,1.6,0.99], 将这些高度顺序连线，会发现有两个山峰，故输出一个2(序列两端不算山峰)
'''

def howManyMountains(h):
	num = 0
	for i in range(1, len(h)-1):
		if h[i]>h[i-1] and h[i]>h[i+1]:
			num += 1
	return num

h = [0.9,1.2,1.22,1.1,1.6,0.99]
print howManyMountains(h)
