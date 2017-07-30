# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:23:30 2016

@author: FANG
"""


class Stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
 