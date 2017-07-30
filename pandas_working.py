# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 13:25:34 2017

@author: FANG
"""


import numpy as np
import pandas as pd
from pandas import DataFrame
H=DataFrame.from_csv(r"C:\Users\FANG\Documents\Automation.csv",encoding="ISO-8859-1",index_col=None)
H.Entity.unique()
H.columns
H=H.rename(columns = {'Remittance Period':'Remittance_Period'})
H.columns=['From_Zip', 'PO_Number', 'Supplier', 'Brand', 'Item', 'Quantity',
       ' EHF_in_Zip ', 'Shipping_Province', 'Order_Date', 'Status',
       'Shipping_Date', 'Unified_Category_Name',
       'Official_Category_in_Province', 'Unit_Amount', 'Total_Amount',
       'Remittance_Period', 'Entity', 'Reserve_one', 'Reserve_Two',
       'Reserve_Three']
H.Remittance_Period.unique()



E1=H['Entity']=='EPRA'
E2=H['Remittance_Period']=='2017-06'
E3=H['Status'].isin(['delivered', 'in transit','Delivered','In Transit','completed','shipped'])
E4=H['Official_Category_in_Province']!='Not Applicable'

EPRA=H[E1 & E2 & E3 & E4]

# or EPRA=H[(H['Entity']=='EPRA') & (H['Remittance_Period']=='2017-06') & (H[H['Status'].isin(['delivered', 'in transit','Delivered','In Transit','completed','shipped'])])]


C1=H['Entity']=='CESA'
C2=H['Remittance_Period']=='2017-06'
C3=H['Status'].isin(['delivered', 'in transit','Delivered','In Transit','completed','shipped'])
C4=H['Official_Category_in_Province']!='Not Applicable'

CESA=H[C1 & C2 & C3 & C4]


EPRAreport=pd.pivot_table(EPRA,index=["Shipping_Province","Official_Category_in_Province"],values=["Quantity","Total_Amount"], aggfunc=np.sum,margins=True)
CESAreport=pd.pivot_table(CESA,index=["Shipping_Province","Official_Category_in_Province"],values=["Quantity","Total_Amount"],aggfunc=np.sum,margins=True)



EPRAreport.loc[[('AB','Laptops,Tablets,Notebooks (after Sep 30/15) '),('BC', 'Micro Toys')]]
EPRAreport.ix[['AB','BC'],'Quantity']

#questions: (1) subtotal (2)parallel