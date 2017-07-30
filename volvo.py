# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 12:51:34 2016

@author: FANG
"""

volvo=pd.read_csv('C:/Users/FANG/Desktop/volvo.txt',sep=';')
X=volvo[['T6','Kilometer']]
Y=volvo[['Price']]

est = sm.OLS(Y, X).fit()