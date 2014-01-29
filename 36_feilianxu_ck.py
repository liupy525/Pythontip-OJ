# !/usr/bin/env python
# -*- coding: utf-8 -*-

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
