# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:46:19 2017

@author: FANG
"""


def seqser(alist,item):
    pos=0
    found=False
    while pos in range(len(alist)) and not found:
        if alist[pos]==item:
            found=True
        else:
            pos=pos+1
    return found
    

def binarysch(alist,item):
    first=0
    last=len(alist)-1
    find=False
    while first<=last and not find:
        middle=(first+last)//2
        if alist[middle]==item:
            find=True
        else:
            if item<alist[middle]:
                last=middle-1
            else:
                first=middle+1
    return find
    



def recbin(alist, item):
    f=0
    if len(alist)==0:
        return False
    else:
        middle=len(alist)//2
        if alist[middle]==item:
            f= True
        elif alist[middle]>item:           
            print(alist[:middle],f)
            return recbin(alist[:middle],item)
            print(alist[:middle],f)
        else:
            print(alist[middle+1:],f)
            return recbin(alist[middle+1:],item)
            print(alist[middle+1:],f)
    
    
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)        
                

                
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self,key,data):
        hashvalue=self.hashfunction(key,len(self.slots))
        print(hashvalue)
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data #replace
            else:
                if self.slots.count(None)==0 and (not key in self.slots):
                    print("Vacancy?")
                    return None
                
                nextslot=self.rehash(hashvalue,len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] !=key:
                    nextslot=self.rehash(nextslot,len(self.slots))
                if self.slots[nextslot]==None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot]=data #replace
    
    def hashfunction(self,key,size):
        return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size
        
    def get(self,key):
        startslot=self.hashfunction(key,len(self.slots))
        
        data=None
        stop=False
        found=False
        position=startslot
        
        while self.slots[position] !=None and not found and not stop:
            if self.slots[position] == key:
                found=True
                data=self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position==startslot:
                    stop=True
        return data
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)


H=HashTable()
for i in range(1,12):
   H[i]='abcdefABCDEI'[i]
   
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)