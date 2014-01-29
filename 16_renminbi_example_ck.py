# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
注明：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。
注意：由于中文乱码问题，输出时请先decode("utf8")，例如你要输出ans = "零圆", print ans.decode("utf8").
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
在中文大写方式中，0到10以及100、1000、10000被依次表示为：
    零壹贰叁肆伍陆柒捌玖拾佰仟万
以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1   壹圆
11  壹拾壹圆
111 壹佰壹拾壹圆
101 壹佰零壹圆
-1000   负壹仟圆
1234567 壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 打印出人民币大写表示
'''

import warnings 
from decimal import Decimal 

def cncapital(value, capital=True, prefix=False, classical=None): 
    ''' 
    人民币数字转汉字表示 Ver 0.03 
    作者: qianjin(AT)ustc.edu 
    版权声明: 
        只要保留本代码最初作者的电子邮件即可，随便用。用得爽的话，不反对请 
    作者吃一顿。 

    参数: 
    capital:    True   大写汉字金额 
                False  一般汉字金额 
    classical:  True   圆 
                False  元 
    prefix:     True   以'人民币'开头 
                False, 无开头 
    ''' 

    # 转换为Decimal 
    if isinstance(value, float): 
        msg = ''' 
        由于浮点数精度问题，请使用考虑使用字符串，或者 decimal.Decimal 类。 
        因使用浮点数造成误差而带来的可能风险和损失作者概不负责。 
        ''' 
        warnings.warn(msg, UserWarning) 
        value = Decimal(str(value)) 
    elif isinstance(value, int): 
        value = Decimal(value) 
    elif not isinstance(value, Decimal): 
        try: 
            value = Decimal(str(value)) 
        except: 
            raise TypeError('无法转换为Decimal：%s' % value.__repr__()) 

    # 截断多余小数 
    value = Decimal(value).quantize(Decimal('0.01')) 

    # 默认大写金额用圆，一般汉字金额用元 
    if classical is None: 
        classical = True if capital else False 

    # 汉字金额前缀 
    if prefix is True: 
        prefix = '人民币' 
    else: 
        prefix = '' 

    # 汉字金额字符定义 
    dunit = ('角', '分') 
    if capital: 
        num = ('零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖') 
        iunit = [None, '拾', '佰', '仟', '万', '拾', '佰', '仟', 
                 '亿', '拾', '佰', '仟', '万', '拾', '佰', '仟'] 
    else: 
        num = ('〇', '一', '二', '三', '四', '五', '六', '七', '八', '九') 
        iunit = [None, '十', '百', '千', '万', '十', '百', '千', 
                 '亿', '十', '百', '千', '万', '十', '百', '千'] 

    if classical: 
        iunit[0] = '圆' if classical else '元' 


    # 处理负数 
    if value < 0: 
        prefix += '负'          # 输出前缀，加负 
        value = - value         # 取正数部分，无须过多考虑正负数舍入 
                                # assert - value + value == 0 

    # 转化为字符串 
    s = str(value) 

    if len(s) > 19: 
        raise ValueError('金额太大了，不知道该怎么表达。') 

    istr, dstr = s.split('.')           # 小数部分和整数部分分别处理 
    istr = istr[::-1]                   # 翻转整数部分字符串 

    so = []     # 用于记录转换结果 

    # 零 
    if value == 0: 
        return prefix + unm[0] + iunit[0] 

    haszero = False     # 用于标记零的使用 
    if dstr == '00': 
        haszero = True  # 如果无小数部分，则标记加过零，避免出现“圆零整” 

    # 处理小数部分 
    # 分 
    if dstr[1] != '0': 
        so.append(dunit[1]) 
        so.append(num[int(dstr[1])]) 
    else: 
        so.append('整')         # 无分，则加“整” 
    # 角 
    if dstr[0] != '0': 
        so.append(dunit[0]) 
        so.append(num[int(dstr[0])]) 
    elif dstr[1] != '0': 
        so.append(num[0])       # 无角有分，添加“零” 
        haszero = True          # 标记加过零了 

    # 无整数部分 
    if istr == '0': 
        if haszero:             # 既然无整数部分，那么去掉角位置上的零 
            so.pop() 
        so.append(prefix)       # 加前缀 
        so.reverse()            # 翻转 
        return ''.join(so) 

    # 处理整数部分 
    for i, n in enumerate(istr): 
        n = int(n) 
        if i % 4 == 0:          # 在圆、万、亿等位上，即使是零，也必须有单位 
            if i == 8 and so[-1] == iunit[4]:   # 亿和万之间全部为零的情况 
                so.pop()                        # 去掉万 
            so.append(iunit[i]) 
            if n == 0:                          # 处理这些位上为零的情况 
                if not haszero:                 # 如果以前没有加过零 
                    so.insert(-1, num[0])       # 则在单位后面加零 
                    haszero = True              # 标记加过零了 
            else:                               # 处理不为零的情况 
                so.append(num[n]) 
                haszero = False                 # 重新开始标记加零的情况 
        else:                                   # 在其他位置上 
            if n != 0:                          # 不为零的情况 
                so.append(iunit[i]) 
                so.append(num[n]) 
                haszero = False                 # 重新开始标记加零的情况 
            else:                               # 处理为零的情况 
                if not haszero:                 # 如果以前没有加过零 
                    so.append(num[0]) 
                    haszero = True 

    # 最终结果 
    so.append(prefix) 
    so.reverse() 
    return ''.join(so) 

print cncapital(100000000)