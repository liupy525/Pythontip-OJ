#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
生活在当代社会，我们要记住很多密码，银行卡，qq，人人，微博，邮箱等等。小P经过一番思索之后，发明了下面这种生成密码方法：
给定两个正整数a和b, 利用a / b我们会到的一个长度无限的小数(若a / b不是无限小数，
比如1/2=0.5,我们认为0.5是0.5000000...，同样将其看做无限长的小数），小P将该小数点后第x位到第y位的数字
当做密码，这样，无论密码有多长，小P只要记住a,b,x,y四个数字就可以了，牢记密码再也不是那么困难的事情了。
现在告诉你a,b,x,y（0 < a,b <= 20132013, 0 < x <= y < 100000000000),请你输出密码。
例如：a = 1, b = 2, x = 1, y = 4, 则 a / b = 0.5000000..., 输出小数点后第1到4位数字，即5000
'''

def xunhuanxiaoshu(a, b):
	l = []
	xunhuan = ['%d' %(a/b), '.']
	dindex = xunhuan.index('.')
	index = 0
	a = a%b
	while True:
		t, a  = divmod(a*10, b)
		temp = (t, a)
		if temp not in l:
			l.append(temp)
			xunhuan.append(str(t))
		else:
			index = l.index(temp)
			break
	return (xunhuan[:dindex+index+1], xunhuan[dindex+index+1:])
	# return ''.join([''.join(xunhuan[:dindex+index+1]), '(', ''.join(xunhuan[dindex+index+1:]), ')'])

# print xunhuanxiaoshu(1231, 65)
print xunhuanxiaoshu(1, 2)
