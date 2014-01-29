# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个list L, 如 L=[2,8,3,50], 对L进行升序排序并输出,
如样例L的结果为[2,3,8,50]
'''

def shengxu(l):
    l.sort()

l = [143,546,23,68,8943,2]
shengxu(l)
print l

# jiangxu
# l.sort(reverse=True)
