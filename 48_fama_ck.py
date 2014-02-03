#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
有一组砝码，重量互不相等，分别为m1、m2、m3……mn；每种砝码的数量有无限个。 
现要用这些砝码去称物体的重量,给你一个重量n,请你判断有给定的砝码能否称出重量n。 
现在给你一个正整数列表w和一个正整数n，列表w中的第i个元素w[i]表示第i种砝码的重量，
n表示要你判断的重量。如果给定砝码能称出重量n，输出Yes，否则输出No。
例如，w=[2,5,11], n=9,则输出Yes（取两个2，一个5）。
'''

def solve(w, n): 
    num=[]
    for i in range(len(w)):  # 初始化num，将无限变换成有限
        num.append(n/w[i])
        m = set()
    for i in range(num[0]+1):  #初始化m
        m.add(w[0]*i)
    for i in range(1,len(num)):
        tmp = m.copy()
        m.clear()
        for j in range(num[i]+1):
            for k in tmp:
                if w[i]*j+k < n:
                    m.add(w[i]*j+k)
                elif w[i]*j+k == n:
                	return "Yes"
    return "No"

w = [2,4,3]
n = 11
print solve(w, n)

