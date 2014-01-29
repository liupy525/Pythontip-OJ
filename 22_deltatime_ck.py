# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给你两个时间st和et(00:00:00<=st <= et<=23:59:59), 请你给出这两个时间间隔的秒数。
如：st="00:00:00", et="00:00:10", 则输出10.
'''

import datetime,time
def dateDiffInSeconds(date1, date2):
    timedelta = date2 - date1
    return timedelta.days*24*3600 + timedelta.seconds

date1 = datetime.datetime(2006,02,17,15,30,00)
date2 = datetime.datetime(2006,05,18,11,01,00)

print dateDiffInSeconds(date1, date2)