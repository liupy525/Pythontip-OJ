#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
有两堆石子，数量任意，可以不同。游戏开始由两个人轮流取石子。游戏规定，每次有两种不同的取法，
一是可以在任意的一堆中取走任意多的石子；二是可以在两堆中同时取走相同数量的石子。最后把石子全部取完者为胜者。
现在给出初始的两堆石子的数目a和b，如果轮到你先取，假设双方都采取最好的策略，问最后你是胜者还是败者。
如果你是胜者，输出Win,否则输出Loose。
例如，a=3,b=1, 则输出Win(你先在a中取一个，此时a=2，b=1,此时无论对方怎么取，你都能将所有石子都拿走).
'''

# 石子问题参考http://www.cnblogs.com/celia01/archive/2011/11/15/2250171.html

import math

p = (math.sqrt(float(5))+1)/float(2)
c = abs(a-b)
if a > b:
    a = b
if a == int(p*c):
    print "Loose"
else: print "Win"
