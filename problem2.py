# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:21:00 2020

@author: jyotm
"""

import sys
line = sys.stdin.readlines()
#print(line)
for c in range(1,int(line[0][:-1])+1):
    lin = line[c][:-1]
    lista = '0' + lin + '0'
    #print(lista)
    op = []
    for i in range(1,len(lista)):
        dif =int(lista[i])-int(lista[i-1])
        #print(dif)
        if dif > 0:
            op.append('('*dif)
        if dif < 0:
            op.append(")"*abs(dif))
        op.append(lista[i])
    op = op[:-1]
    #print(op)
    fin = "".join(op)
    print("case #"+ str(c)+":", fin)