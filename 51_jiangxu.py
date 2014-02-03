#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个list L, 如 L=[2,8,3,50], 对L进行降序排序并输出,
如样例L的结果为[50,8,3,2]
'''

def jiangxu(L):
	return sorted(L, reverse = True)

L = [50, 8, 3, 2]
print jiangxu(L)
