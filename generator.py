# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:32:00 2016

@author: FANG
"""


def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
        

n = 0
g = triangles()
for t in g:
    print(t)
    n = n + 1
    if n == 10:
        break
    
    
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0);
        L = [L[i-1] + L[i] for i in range(len(L))]
        
        
        
        
L[0]+L[1],L[1]+L[2]
L[0]+L[1],L[1]+L[2],L[2]+L[3]