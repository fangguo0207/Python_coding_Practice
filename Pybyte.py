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


def func(x):
    x
    
    print('x is', x)
    x = 2 
    print('Changed local x to', x)

func(x)
print('x is still', x)


def func():
    global x
    
    print('x is', x)
    x = 2 
    print('Changed global x to', x)

func()
print('value of x is', x)




def say(message, times=1):
    print(message*times)

say('A',10)






def total(a=5, *numbers, **phonebook):
    print('a', a)

    #iterate through all the items in tuple
    for single_item in numbers:
        print('single_item', single_item)

    #iterate through all the items in dictionary    
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

def maximum(x,y):
    if x>y:
        return x
    elif x==y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2,3))




def print_max(x,y):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    # convert to integers, if possible
    x=int(x)
    y=int(y)
    if x>y:
        print(x, 'is maximum')
    else:
        print(y, 'is maxium')
print_max(3,5)
print(print_max.__doc__)




