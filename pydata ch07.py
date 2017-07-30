# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 23:28:31 2016

@author: FANG
"""



def say_hello():
    print('hello world')
    
    

def print_max(a,b):
    if a>b:
        print(a,'is maximum')
    elif a==b:
        print(a, 'is equal to', b)
    else:
        print(b,'is maximum')

x=50

def func():
    global x
    
    print('x is', x)
    x = 2 
    print('Changed global x to', x)

func()
print('value of x is ', x)