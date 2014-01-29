# !/usr/bin/env python
# -*- coding: utf-8 -*-

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