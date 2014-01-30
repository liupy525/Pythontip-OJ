# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
有一组砝码，重量互不相等，分别为m1、m2、m3……mn；它们可取的最大数量分别为x1、x2、x3……xn。 
现要用这些砝码去称物体的重量,问能称出多少种不同的重量。 
现在给你两个正整数列表w和n， 列表w中的第i个元素w[i]表示第i个砝码的重量，列表n的第
i个元素n[i]表示砝码i的最大数量。i从0开始，请你输出不同重量的种数。
如：w=[1,2], n=[2,1], 则输出5（分析：共有五种重量：0,1,2,3,4）
'''

def zhongshu(weight, number):
	w = set()
	for i in range(number[0]+1):
		w.add(weight[0]*i)
	for i in range(1, len(weight)):
		temp = w.copy()
		w.clear()
		for temp_weight in temp:
			for k in range(number[i]+1):
				w.add(temp_weight + weight[i]*k)
	return len(w)

w, n = [1,2], [2,1]

print zhongshu(w, n)
