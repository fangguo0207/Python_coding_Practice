# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 15:39:06 2019

@author: FangGuo
"""


import pyodbc
import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 60)
pd.set_option('display.width', 300)
connection = pyodbc.connect(r'DSN=SCHCASQL8; Database = SCHCARPT')
cursor=connection.cursor()

tables = [table for table in list(cursor.tables())]
len(tables)

Inventory = pd.read_sql("SELECT CAST(QUERYDATE AS DATE) AS DATE, PRDUCT, VERSN, TOTALQTY FROM WF.INVENTORY_TRACKING",con=connection)
#Inventory = Inventory.drop_duplicates(['DATE', 'PRDUCT', 'VERSN'], keep = 'first')
Inventory.PRDUCT = Inventory.PRDUCT.astype('str').replace('\.0', '', regex=True)
Inventory.VERSN = Inventory.VERSN.astype('str').replace('\.0', '', regex=True)
Inventory.TOTALQTY = Inventory.TOTALQTY.astype('int')

InventoryReport = pd.pivot_table(Inventory, values = ['TOTALQTY'], index = ['PRDUCT', 'VERSN'], columns = ['DATE'], aggfunc={'TOTALQTY':sum})
InventoryReport

InventoryReport['VLA'] = InventoryReport.std(axis=1)
InventoryReport['MEAN'] = InventoryReport.mean(axis=1)
