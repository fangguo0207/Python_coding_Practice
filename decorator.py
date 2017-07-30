# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 21:34:40 2016

@author: FANG
"""


def getTalk(type="shout"):
    def shout(word="yes"):
        return word.capitalize()+"!"
    
    def whisper(word="yes"):
        return word.lower()+"..."
        
    if type=="shout":
        return shout
    else:
        return whisper
    
def doSomethingBefore(func):
    print("I do something before then I call the function you gave me")
    print(func())


def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():
        print("Before the function runs")
        a_function_to_decorate()
        print("After the function runs")
    return the_wrapper_around_the_original_function



def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("</''''''\>")
    return wrapper
    
def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper
    

def sandwich(food="---veggie---"):
    print(food)



def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1,arg2):
        print("I got args! Look:", arg1, arg2)
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments
    
@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("My name is", first_name, last_name)
    
    
    
def method_friendly_decorator(method_to_decorate):
    def wrapper(self,lie):
        lie=lie-3
        return method_to_decorate(self,lie)
    return wrapper
    
