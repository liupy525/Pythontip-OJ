# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个list L, 如 L=[0,1,2,3,4], 输出L的中位数（若结果为小数，则保留一位小数）。
'''

L = [1,2,3,3.3,5,6]

n = len(L)
L.sort()
if n%2==0:
    print "%.1f" %((L[n/2-1]+L[n/2]+0.0)/2)
else:
    print L[(n-1)/2]

