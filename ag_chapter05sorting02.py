# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 09:49:18 2017

@author: FANG
"""


def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
   return alist
   
   
def shellSort(alist):
    sublistcount=len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition,sublistcount)
        print("After increments of size", sublistcount, "The list is", alist)
        
        sublistcount=sublistcount//2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue=alist[i]
        position=i
        
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position - gap
        
        alist[position]=currentvalue
        
    
                
    