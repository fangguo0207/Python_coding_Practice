# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 15:20:11 2018

@author: fangguo
"""


import pyodbc
import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 100)
pd.reset_option('display.max_columns')       
pd.set_option('display.width', 300)




#connect to the database in use
connection = pyodbc.connect(r'DSN=SCHCASQL8; Database = SCHCARPT')
cursor=connection.cursor()

# Get the full list of tables
tables = [table for table in list(cursor.tables())]
len(tables)

#a function that list the first tables, number is how many tables listed
def table_list(the_object, number:int):
    a=0
    for i in the_object:
        if a<=number:
            print(i)
            a+=1
        else:
            break
#Query to get Top rows the table "Picker_stats"
#Pickers=pd.read_sql("select Top 1000000 * from backend.Picker_stats", con=connection)
#Pickers2=pd.read_sql("select top 2000000 * from backend.Picker_stats except select top 1000000 * from backend.Picker_stats", con=connection)

#Query to get rows amid the table "Picker_stats"
##test=pd.read_sql("select Top 1000 * from backend.Picker_stats Except select top 600 * from backend.Picker_stats", con=connection)

#check the shape of a column
##for i in Pickers['Operator'].unique():
##    print({i:Pickers[Pickers['Operator']==i].shape})
            

#pickers[(Pickers['Area']=='Tower') & (Pickers['Operator'] == 'picker a')]
#pickexample=Pickers[Pickers['Operator'].isin(['Operator June Rothwell','Operator Neil Dixon'])]

Pickers = pd.read_sql("SELECT XAC_ID, CREATION_TIMESTAMP, YEAR(CREATION_TIMESTAMP) as YEAR,  MONTH(CREATION_TIMESTAMP) as MONTH, DAY(CREATION_TIMESTAMP) as DAY, [TYPE], CAR_LABEL, IOH_ID, OID_ID, PLO_ID, MSG_TEXT FROM SCHCARPT.RDCUSR.XAC WHERE MSG_TEXT LIKE '%PICKED%' AND MSG_TEXT LIKE '%Operator%' AND CREATION_TIMESTAMP > '20180501' ORDER BY CREATION_TIMESTAMP DESC", con=connection)
Pickers_new = Pickers.copy()

import re
def get_picker(t):
    t1=re.findall('Operator \D+ has', t)[0]
    t1=t1.replace('Operator ','')
    t1=t1.replace(' has','')
    return t1
    
def get_qty(t):
    t1=re.findall('Quantity \d+',t)[0]
    t1=t1.replace('Quantity ','')
    return int(t1)

def get_totalqty(t):
    t1=re.findall('\(of \d+\)',t)[0]
    t1=t1.replace('(of ','')
    t1=t1.replace(')','')
    return int(t1)

def get_SKU(t):
    t1=re.findall('SKU \d+',t)[0]
    t1=t1.replace('SKU ','')
    return t1

def get_Carrier(t):
    t1=re.findall('Carrier \d+',t)[0]
    t1=t1.replace('Carrier ','')
    return t1

def get_Order(t):
    t1=re.findall('Order [A-Z]{0,5}\d+',t)[0]
    t1=t1.replace('Order ','')
    return t1

def get_zone(t):
    t1=re.findall('zone [A-Z0-9]+', t, re.IGNORECASE)[0]
    t1=t1.replace('zone ','')
    return t1

def get_location(t):
    t1=re.findall('slot [A-Z0-9]+', t, re.IGNORECASE)[0]
    t1=t1.replace('slot ','')
    return t1

def find_picker(t):
    t1=re.findall('Operator \D+ has', t)
    return len(t1)

def find_area(t):
    return t[0:2]


Pickers_new['Picker'] = Pickers_new['MSG_TEXT'].apply(get_picker)
Pickers_new['Picking_qty']=Pickers_new['MSG_TEXT'].apply(get_qty)
Pickers_new['Total']=Pickers_new['MSG_TEXT'].apply(get_totalqty)
Pickers_new['SKU']=Pickers_new['MSG_TEXT'].apply(get_SKU)
Pickers_new['Carrier_number']=Pickers_new['MSG_TEXT'].apply(get_Carrier)
Pickers_new['Order_number']=Pickers_new['MSG_TEXT'].apply(get_Order)
Pickers_new['Zone'] = Pickers_new['MSG_TEXT'].apply(get_zone)
Pickers_new['Location'] = Pickers_new['MSG_TEXT'].apply(get_location)
Pickers_new['Weekday_name']=Pickers_new['CREATION_TIMESTAMP'].dt.weekday_name
Pickers_new['Hours'] = Pickers_new.CREATION_TIMESTAMP.dt.hour
Pickers_new['Shift'] = np.where(Pickers_new['Hours']<12, 'morning','afternoon')
Pickers_new['Shift'] = np.where(Pickers_new['Hours']>17, 'evening',Pickers_new['Shift'])
Pickers_new['Area'] = Pickers_new.Zone.apply(find_area)



Pickers_new = Pickers_new[['XAC_ID', 'CREATION_TIMESTAMP', 'YEAR', 'MONTH', 'DAY', 'Weekday_name', 'Hours', 'TYPE', 'CAR_LABEL', 'IOH_ID', 'OID_ID', 'PLO_ID', 'MSG_TEXT', 'Picker', 'Picking_qty', 'Total', 'SKU', 'Carrier_number', 'Order_number', 'Zone', 'Location',  'Shift', 'Area']]
Pickers_new = Pickers_new.sort_values(['Picker','CREATION_TIMESTAMP'])
#Pickers_test = Pickers_new.copy()

Pickers_new['compare'] = Pickers_new['CREATION_TIMESTAMP'].shift(1)
Pickers_new['Pace'] = Pickers_new['CREATION_TIMESTAMP']-Pickers_new['compare']
Pickers_new['Pace'] = Pickers_new['Pace'].dt.seconds
#Pickers_new[:100].to_csv(r'C:\Users\fangguo\Desktop\picker_test.csv', index = False)
Pickers_new['Match_Picker'] = Pickers_new['Picker'] == Pickers_new['Picker'].shift(1)
Pickers_new = Pickers_new[Pickers_new['Match_Picker']]


# AREA sight
Pickers_test = Pickers_new[Pickers_new['Pace']<1000]
Pickers_TR = Pickers_test[Pickers_test['Area']=='CS']
print(Pickers_TR.shape)
print(Pickers_TR.groupby(by='MONTH')['Pace'].describe())

Pickers_BC = Pickers_test[Pickers_test['Area']=='BC']
print(Pickers_BC.shape)
print(Pickers_BC.groupby(by='MONTH')['Pace'].describe())

Pickers_ED = Pickers_test[Pickers_test['Area']=='CE']
print(Pickers_ED.shape)
print(Pickers_ED.groupby(by='MONTH')['Pace'].describe())

Pickers_FP = Pickers_test[Pickers_test['Area']=='FP']
print(Pickers_FP.shape)
print(Pickers_FP.groupby(by='MONTH')['Pace'].describe())


TR_opr = Pickers_TR['Picker'].unique()
TR_opr = [opr for opr in TR_opr if Pickers_TR[Pickers_TR['Picker']==opr].shape[0]>500]
Pickers_TR_sense = Pickers_TR[Pickers_TR['Picker'].isin(TR_opr)]
TR_pivot = pd.pivot_table(Pickers_TR_sense, values = ['Pace', 'Picking_qty'], index = ['Picker', 'MONTH'], aggfunc={'Pace': np.mean,'Picking_qty': ['count', max, np.mean]})


P1 = np.array(Pickers_new[(Pickers_new['Pace'] >= 1000) & (Pickers_new['Pace'] < 10000)].index)
Rownum = np.array([Pickers_new.index.get_loc(r) for r in list(P1)])
R1 = Rownum + 1
R2 = Rownum - 1
Rownum = list(np.concatenate((Rownum,R1,R2)))
Rownum = sorted(list(set(Rownum)))
Pickers_long = Pickers_new.iloc[Rownum]
Pickers_long.to_csv(r'C:\Users\fangguo\Desktop\picker_test.csv', index = False)



Pickers_new = Pickers_new[Pickers_new['Pace'] < 1000]
print(Pickers_new.shape)




Operators=Pickers_new['Operator'].unique()
selection=np.random.choice(Operators, 5)
test=Pickers_new[Pickers_new['Operator'].isin(selection)]


import seaborn as sns
sns.set(style="ticks", palette="pastel")
sns.set(rc={'figure.figsize':(15,9.3)})

sns.boxplot(x="Operator", y="dif", hue='Area', palette=["m", "g"], data=test)









# 备用
#pickers['CREATION_TIMESTAMP']=pickers['CREATION_TIMESTAMP'].apply(str)
#pickers['CREATION_TIMESTAMP']=pd.to_datetime(pickers['CREATION_TIMESTAMP'],errors='coerce')
#tower=Pickers_new[Pickers_new['Area']=='Tower']
#tower['location_compare']=tower['PLO_ID'].shift(1)
#tower['height']=np.where(tower['PLO_ID'].apply(lambda x: x[2]).isin(['1','2','3','4']),2,1)
#tower['height_compare']=np.where(tower['location_compare'].apply(str).apply(lambda x: x[2]).isin(['1','2','3','4']),2,1)
#tower['run']=np.where(tower['height_compare']==tower['height'],'No','Yes')
#pickers['dif']=pickers['dif'].dt.seconds
#pickers_refine['compare']=pd.to_datetime(pickers_refine['compare'])

#connect to default database and why? Database = SCHCARPT looks like not helpful
#https://stackoverflow.com/questions/49259839/pyodbc-always-connects-to-master-database
#--connection_a = pyodbc.connect(r'Driver=SQL Server; Server=SCHCASQL8; Database = SCHCARPT')
#--cursor_a=connection_a.cursor()


