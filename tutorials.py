# -*- coding: utf-8 -*-
"""
Created on Sun May 14 22:34:13 2017

@author: FANG
"""


def yangpascal_a(n):
    L=[1]
    for i in range(n):
        yield L
        L=[1]+[L[j]+L[j+1] for j in range(i)]+[1]
           
           
        
def yangpascal_b(n):
    if n == 0:
        return [1]
    else:
        return [1]+[yangpascal_b(n-1)[j]+yangpascal_b(n-1)[j+1] for j in range(n-1)]+[1]
    

        
def yangpascal_c(n):
    if n == 0:
        return [1]
    else:
        return [i+j for i, j in zip ([0]+yangpascal_c(n-1),yangpascal_c(n-1)+[0])]