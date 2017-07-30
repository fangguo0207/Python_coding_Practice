# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:03:33 2017

@author: FANG
"""


def bubble_sort(alist):
    x=0
    for i in range(len(alist)-1):
        for j in range(len(alist)-i-1):
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1]=alist[j+1],alist[j]
                x=x+1
            if x==0:
                return "sorted"
        print(alist)
    return alist,x
    
bubble_sort([0,1,1,2,3,6])




def select_sort(alist):
    for i in range(len(alist)):
        che=alist[0]
        for j in range(len(alist)-i-1):
            if alist[j+1]>=che:
                che=alist[j+1]
            print(i,j)
        alist.remove(che)
        alist.insert(len(alist)-i,che)
    return alist

select_sort(list(random.sample(range(101),20)))



def select_sortb(alist):
    for i in range(len(alist)-1,0,-1):
        count=0
        for j in range(i+1):
            if alist[j]>=alist[count]:
                count=j    
            print(i,j,count,alist)
        alist[count],alist[i]=alist[i],alist[count]
        print(alist)
    return alist

import random    
select_sortb(list(random.sample(range(1,500),20)))