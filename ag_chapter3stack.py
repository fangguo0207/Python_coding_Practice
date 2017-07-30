# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 14:45:12 2017

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



from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    opStack=Stack()
    postfixList=[]
    tokenList=infixexpr.split()
    
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
            print(opStack.items)
        elif token=='(':
            opStack.push(token)
            print(opStack.items)
        elif token==')':
            topToken=opStack.pop()
            while topToken!='(':
                postfixList.append(topToken)
                topToken=opStack.pop()
                print(opStack.items)
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()]>=prec[token]):
                print(opStack.items)
                postfixList.append(opStack.pop())
            opStack.push(token)
            print(opStack.items)
    while not opStack.isEmpty():
            postfixList.append(opStack.pop())
    return "".join(postfixList)
print(infixToPostfix("( A + B ) * C - ( D - E + F ) * ( G + H )"))
    




def calculation(z,x,y):
    if z=="+":
        return x+y
    elif z=="-":
        return x-y
    elif z=="*":
        return x*y
    elif z=="/":
        return x/y
    elif z=="**":
        return x**y

from pythonds.basic.stack import Stack



def postfixvalue(postfixExpr):
    valueStack=Stack()
    tokenlist=postfixExpr.split()
    print(tokenlist)
    for token in tokenlist:
        if token in list(map(str,list(range(100)))):
            valueStack.push(int(token))
            print(valueStack.items)
        else:
            c1=valueStack.pop()
            c2=valueStack.pop()
            valueStack.push(calculation(token,c2,c1))
    return valueStack.items  
    
    
    
    
    
def infixToPostfix2(infixexpr):
    prec={}
    prec["**"]=3
    prec["*"]=2
    prec["/"]=2
    prec["+"]=1
    prec["-"]=1
    prec["("]=0
    opStack=Stack()
    postfixList=[]
    tokenList=infixexpr.split()
    
    for token in tokenList:
        if token in list(map(str,list(range(100)))):
            postfixList.append(token)
            print(opStack.items)
        elif token=='(':
            opStack.push(token)
            print(opStack.items)
        elif token==')':
            topToken=opStack.pop()
            while topToken!='(':
                postfixList.append(topToken)
                topToken=opStack.pop()
                print(opStack.items)
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()]>=prec[token]):
                print(opStack.items)
                postfixList.append(opStack.pop())
            opStack.push(token)
            print(opStack.items)
    while not opStack.isEmpty():
            postfixList.append(opStack.pop())
    return " ".join(postfixList)

