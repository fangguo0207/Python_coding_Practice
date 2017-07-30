# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


class Queue():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self,num):
        return self.items.pop(num)
    def size(self):
        return len(self.items)
        


#print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
def whowin(squad,number):
    team=Queue()
    for teammate in squad:
        team.enqueue(teammate)
    while team.size()>1:
        num=0
        while num<number:
            team.enqueue(team.dequeue(team.size()-1))
            num=num+1
        team.dequeue(team.size()-1)
        print(team.items)
    return team.items
    
print(whowin(["Bill","David","Susan","Jane","Kent","Brad"],7))

class Printer:
    def __init__(self,ppm):
        self.pagerate=ppm
        self.currentTask=None
        self.timeRemaining=0     
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining=self.timeRemaining-1
            if self.timeRemaining <= 0:
                self.currentTask=None
        
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startNext(self,newtask):
        self.currentTask=newtask
        self.timeRemaining = newtask.getPages()*60/self.pagerate
        

import random

class Task:
    def __init__(self,time):
        self.timestamp=time
        self.pages=random.randrange(1,21)
    def getStamp(self):
        return self.timestamp
    def getPages(self):
        return self.pages
    def waitTime(self,currenttime):
        return currenttime - self.timestamp
        

from pythonds.basic.queue import Queue

def newPrintTask():
    num=random.randrange(1,181)
    if num==180:
        return True
    else:
        return False
        
        





def simulation(numSeconds,pagesPerMinute):
    
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes=[]

    for currentSecond in range(numSeconds):
        
        if newPrintTask():
            task=Task(currentSecond)
            printQueue.enqueue(task)
            
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask=printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        
        labprinter.tick()
        
    averageWait=sum(waitingtimes)/len(waitingtimes)
    
    print("Average Wait %6.5f secs %3d tasks remaining."%(averageWait, printQueue.size()))
    
                