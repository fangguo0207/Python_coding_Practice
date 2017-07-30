# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:21:10 2016

@author: FANG
"""




class Robot:
    population=0
    
    def __inti__(self,name):
        self.name=name
        print("(Initializing {})".format(self.name))        
        Robot.population+=1
    
    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -=1

        if Robot.population==0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))
        
    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))
    

