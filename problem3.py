# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:47:52 2020

@author: jyotm
"""

import sys
import numpy as np
line = sys.stdin.readlines()
#print(line)
ind = 2
for ct in range(1,int(line[0][:-1])+1):
    n = int(line[ind-1][:-1])
    i = 0
    s = np.zeros(n)
    e = np.zeros(n)
    for row in range(ind,ind + n):
        s[i], e[i] = np.array(line[row][:-1].split(" ")).astype('int')
        i+=1
    ind+=n+1
    #print(s, e)
    e = [x for _,x in sorted(zip(s,e))]
    index = [x for x,_ in sorted(zip(range(len(s)),s), key=lambda pair: pair[1])]
    s = sorted(s)
    
    c = -1
    j = -1
    st = []
    flg = 0
    for i in range(0,len(s)):
        if(e[c] <= s[i] or c==-1):
            c = i
            st.append("C")
        elif e[j] <= s[i] or j==-1 :
            j = i
            st.append("J")
        else :
            st = "IMPOSSIBLE"
            flg = 1
            break;
    
    if( flg != 1):    
        st = [x for _,x in sorted(zip(index,st))]
        print("Case #"+ str(ct)+":","".join(st))
    else:
        print("Case #"+ str(ct)+": "+st)
    