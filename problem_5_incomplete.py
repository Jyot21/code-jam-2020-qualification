# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:55:05 2020

@author: jyotm
"""

import sys

def print_mat(n,na,k):
    
    for i in range(1, n+1):
        print(" ".join(map(str,na)))
        end = na[-1]
        na[1:] = na[:-1] 
        na[0] = end

import numpy as np

def checkValueAtIndex(arr, value, i, j):
    if arr[i][j] == value or arr[j][i] == value:
        return False
    return True
line = sys.stdin.readlines()
#print(line)

for ct in range(1,int(line[0][:-1])+1):
    lin = line[ct][:-1].split(" ")
    n = int(lin[0])
    tr = int(lin[1])
    if ( tr%n == 0):
        print("Case #"+ str(ct)+": POSSIBLE")
        k = tr//n
        lista = [x for x in range(1,n+1)]
        print_mat(n,lista, k)
    else:
        print("Case #"+ str(ct)+": IMPOSSIBLE")
