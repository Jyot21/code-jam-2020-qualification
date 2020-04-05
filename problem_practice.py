# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 10:23:05 2020

@author: jyotm
"""

import sys,math
line = sys.stdin.readlines()
#print(line)
for c in range(1,int(line[0][:-1])+1):
    n = int(line[c][:-1])
    digits = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
    #print(digits)
    d1 = [2 if i == 4 else i for i in digits]
    d2 = [2 if i == 4 else 0 for i in digits]
    res = int("".join(map(str, d1)))
    res2 = int("".join(map(str, d2)))
    print("case #"+ str(c)+":", res, res2)
    