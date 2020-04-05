# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:16:51 2020

@author: jyotm
"""


import sys,math
import numpy as np
line = sys.stdin.readlines()
ind = 2
for c in range(1,int(line[0][:-1])+1):
    n = int(line[ind-1][:-1])
    matrix = np.zeros((n,n))
    i = 0
    for row in range(ind,ind + n):
        matrix[i,:] = np.array(line[row][:-1].rsplit(" ")).astype(int)
        i+=1
    ind += n+1
    #print(matrix)
    tr = int(np.trace(matrix))
    
    r = 0; c = 0
    for i in range(n):
        if len(matrix[i,:]) != len(np.unique(matrix[i,:])):
            r+=1
        if len(matrix[:,i]) != len(np.unique(matrix[:,i])):
            c+=1
    print("case #"+ str(c)+":", tr, r,c)
    
'''     
    digits = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
    #print(digits)
    d1 = [2 if i == 4 else i for i in digits]
    res = int("".join(map(str, d1)))
    res2 = int("".join(map(str, d2)))
    print("case #"+ str(c)+":", res, res2)
    d2 = [2 if i == 4 else 0 for i in digits]'''
    