# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 23:09:16 2016

@author: FANG
"""

class A(object):  
    # 实例方法  
   def foo(self,x):  
       print( "executing foo(%s,%s)"%(self,x)) 
    # 类方法  
   @classmethod  
   def class_foo(cls,x):  
       print ("executing class_foo(%s,%s)"%(cls,x))
    # 静态方法  
   @staticmethod  
   def static_foo(x):  
       print ("executing static_foo(%s)"%x)  
  
a = A()  

class OA:
    def __init__(self):
        pass
    def change_a(self,a):
        self.a = a

class CA:
    a=0
    @classmethod
    def change_a(cls,a):
        cls.a=a
        
class SA:
    a=0
    @staticmethod
    def change_a(a):
        return a