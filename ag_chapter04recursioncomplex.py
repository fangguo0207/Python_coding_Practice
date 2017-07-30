# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 21:19:56 2017

@author: FANG
"""


def moveTower(height,fromPole,toPole,withPole):
    if height>=1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
    
def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

    
moveTower(3,"A","B","C")



def dpMakeChange(coinValueList,change,minCoins):
    changeadd=[0]*(change+1)
    for cents in range(change+1):
        coinCount = cents
        changeadd[cents]=1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                changeadd[cents]=j
        minCoins[cents] = coinCount
    return changeadd
   
    
def track(coinValueList,num):
    use=dpMakeChange(coinValueList,num,[0]*(num+1))
    if num in use:
        return [use[num]]
    else:
        return [use[num]]+track(coinValueList,num-use[num])
    
    
    
    


    
   
        
def Triangle(row):
    if row<1:
        return "please input an integer greater than 1"
    if row==1:
        return [1]
    else:
        return [1]+[Triangle(row-1)[i]+Triangle(row-1)[i+1] for i in range(row-2)]+[1]