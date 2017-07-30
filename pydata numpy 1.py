# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 19:15:01 2016

@author: FANG
"""
import numpy as np
data1=[6,7.5,8,0,1]
arr1=np.array(data1)
data2=[[1,2,3,1,2,3],[5,6,7,8,9,10]]
arr2=np.array(data2)
int_array=np.arange(10)
calibers=np.array([.22,.270,.357,.380,.44,.50],dtype=np.float64)
int_array.astype(calibers.dtype)
names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
import matplotlib.pyplot as plt