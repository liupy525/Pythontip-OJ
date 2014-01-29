# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个非连续子序列，使其和最大，输出最大子序列的和。
这里非连续子序列的定义是，子序列中任意相邻的两个数在原序列里都不相邻。
例如，对于L=[2,-3,3,50]， 输出52（分析：很明显，该列表最大非连续子序列为[2,50]).
'''

def maxSum(L):
	if len(L) >= 2:
	    dp=[L[0],max(L[0],L[1])]
	    for i in range(2,len(L)):
	        # dp.append(max(dp[i-1],max(L[i]+dp[i-2],L[i])))
	        dp.append(max(dp[i-1],L[i]+dp[i-2]))
	    return dp[len(L)-1]
	else:
	    return L[0]

L = [2,-3,3,50]
# L = [-1, -1, -1, -1, 0]
print maxSum(L)
