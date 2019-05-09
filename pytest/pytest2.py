# -*- coding: UTF-8 -*-
'''
Created on 2019年4月27日

@author: 13892
'''
import math


def verify(num):
    return ('float', 'int')[round(float(num)) == float(num)]

def successive_num(n):
    lst = []
    for i in xrange(1, n):
        z = 2 * n + i * i - i
        y_1 = (-1 + math.sqrt(1 + 4 * z)) / 2
        y_2 = (-1 - math.sqrt(1 + 4 * z)) / 2
        if y_1 > 0 and verify(y_1) == "int":
            lst.append(" ".join([str(i) for i in xrange(i, int(y_1) + 1)]))
        if y_2 > 0 and verify(y_2) == "int":
            lst.append(" ".join([str(i) for i in xrange(i, int(y_1) + 1)]))
    if lst:
        return "\n".join(lst)
    else:
        return "NONE"

if __name__ == '__main__':
    n = int(raw_input())
    print(successive_num(n))
