# !/usr/bin/env python
# -*- coding: utf-8 -*-

decimals = []
if a > b :
a =a%b
cnt = 0
flag = False
x-=1
y-=1
while cnt <= y:
    decimalPart,a = divmod(a*10**1024,b)
    if flag:
        decimals.append(str(decimalPart).zfill(1024))
    if x >= cnt and x < cnt+1024:
        flag = True
        decimals.append((str(decimalPart).zfill(1024))[x-cnt:])
    if y>=cnt and y< cnt+1024:
        break
    cnt +=1024
if y/1024 !=x/1024:
    decimals[-1]=(str(decimals[-1]))[:y-cnt+1]
else:
    decimals[-1]=(str(decimals[-1]))[:y-x+1]
print ''.join(decimals)