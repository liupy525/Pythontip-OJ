# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你一个字符串a和一个正整数n,判断a中是否存在长度为n的回文子串。如果存在，则输出YES，否则输出NO。
回文串的定义：记串str逆序之后的字符串是str1，若str=str1,则称str是回文串，如"abcba".
'''

def huiwen(a, n):
	l = list(a)
	for i in range(0, len(l)-n+1):
		k = l[i:i+n]
		m = l[i:i+n]
		m.reverse()
		if m==k:
			return True
	return False

print huiwen('1234355', 3)