# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:01:33 2019

@author: FangGuo
"""

import pyodbc
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 100)
#pd.reset_option('display.max_columns')       
pd.set_option('display.width', 300)




#connect to the database in use
connection = pyodbc.connect(r'DSN=SCHCASQL8; Database = SCHCARPT')
cursor=connection.cursor()

tp = pd.read_csv(r"C:\Users\fangguo\Documents\Carrier\UPS Invoices.csv", low_memory=False, chunksize=1000)
UPS = pd.concat(tp, ignore_index=True)
