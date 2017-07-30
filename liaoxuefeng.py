# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 21:32:00 2016

@author: FANG
"""


def tower(n,a,b,c):
    if n==1:
        print(a,"--->",b)
    if n==2:
        print(a,"--->",c)
        print(a,"--->",b)
        print(c,"--->",b)
    else:
        print(tower(n-1,a,c,b))
        print(a,"--->",b)
        print(tower(n-1,c,b,a))