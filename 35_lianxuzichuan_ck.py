# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个整数list L, 如 L=[2,-3,3,50], 求L的一个连续子序列，使其和最大，输出最大子序列的和。
例如，对于L=[2,-3,3,50]， 输出53（分析：很明显，该列表最大连续子序列为[3,50]).
'''

def maxSubSum(L):
    maxSum,thisSum= 0,0
    for item in L:
        thisSum += item;
        if thisSum > maxSum:
            maxSum = thisSum
        elif thisSum < 0:
            thisSum = 0
    return maxSum

L = [2,-3,3,50,43,123,-34,67,3,458,97,3,-342,675,3,67,98,34,23,67,7,34,-9,-23293,342,23,56,78,423,-213,34,67,8]

print maxSubSum(L)