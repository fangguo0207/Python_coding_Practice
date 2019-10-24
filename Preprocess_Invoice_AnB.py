# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:04:31 2019

@author: FangGuo
"""


import glob, os
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 300)

directory = r'\\Schcasql8\ssis\Invoice_Files\AnB'
os.chdir(directory)
for filename in glob.glob("*.csv"):
    print(filename)
    process_file = directory + '\\' + filename
    print(process_file)
    invoice=pd.read_csv(process_file, encoding='iso-8859-1')

    invoice.columns = ['_'.join(col.split(' ')) for col in list(invoice.columns)]

    invoice['Account'] = np.nan
    invoice['COST_PER_LB'] = invoice['SubTotAmt']/invoice['Weight']
    invoice['COST_PER_LB'] = invoice['COST_PER_LB'].apply(lambda x: float("{0:.2f}".format(x)))
    invoice['SHIP_MONTH2'] = np.nan
    invoice['SHIP_YEAR2'] = np.nan
    invoice['Individual'] = np.nan

    
    invoice.to_csv(process_file, index=False)


