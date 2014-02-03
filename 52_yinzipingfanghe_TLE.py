#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
6 的因子有 1, 2, 3 和 6, 它们的平方和是 1 + 4 + 9 + 36 = 50. 如果 f(N) 代表正整数 N 所有因子的平方和, 那么 f(6) = 50.
现在令 F 代表 f 的求和函数, 亦即 F(N) = f(1) + f(2) + .. + f(N), 显然 F 一开始的 6 个值是: 1, 6, 16, 37, 63 和 113.
那么对于任意给定的整数 N (1 <= N <= 10^8), 输出 F(N) 的值.
'''

# 参考http://bbs.byr.cn/#!article/ACM_ICPC/75724
# 不要一个一个算，整体来看，F(N)必然包括N个1**2，N//2个2**2,N//3个3**2.... 
# 然后从N/2+1开始，就只有一个n**2，在统计2**2时可以统计出相应的（N//2）**2，优化一下么就可以O（sqrt（N））做到 

def F(N):
	s = 0
 	for i in range(1, N/2+1):
 		# if float(N)/i==N/i:
	 	# 	s += N * i
	 	# else:
	 	# 	s += N/i * i**2
	 	s += N * i - N%i * i
 		# print s
 	for i in range(N/2+1, N+1):
 		s += i**2
 		# print s
 	return s

print F(5)

