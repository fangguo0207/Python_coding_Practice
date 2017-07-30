# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 09:49:18 2017

@author: FANG
"""


def insertionsort(alist):
    for i in range(1,len(alist),1):
        print(i)
        for j in range(i,-1,-1):
            print(j)
            toinsert=alist[j]
            if toinsert<alist[j-1]:
                toinsert, alist[j-1]=alist[j-1], toinsert
    return alist
                
    