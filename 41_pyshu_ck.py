#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Py从小喜欢奇特的东西，而且天生对数字特别敏感，一次偶然的机会，他发现了一个有趣的四位数2992，
这个数，它的十进制数表示，其四位数字之和为2+9+9+2=22，它的十六进制数BB0，其四位数字之和也为22，
同时它的十二进制数表示1894，其四位数字之和也为22，啊哈，真是巧啊。
Py非常喜欢这种四位数，由于他的发现，所以这里我们命名其为Py数。
现在给你一个十进制4位数n，你来判断n是不是Py数，若是，则输出Yes，否则输出No。
如n=2992，则输出Yes； n = 9999，则输出No。
'''

def getSumByValue(n,value):
    res = 0
    while n:
        res += n%value
        n /=value
    return res

if getSumByValue(n,10) == getSumByValue(n,16) == getSumByValue(n,12):
    print 'Yes'
else:
    print 'No'
