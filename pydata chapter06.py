# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 23:13:08 2016

@author: FANG
"""


import pandas as pd
import numpy as np
f1=pd.read_csv("C:/Python/pydata/ch06/ex1.csv")

list(open("C:/Python/pydata/ch06/ex3.txt"))

import warnings
warnings.simplefilter(action = "ignore", category = RuntimeWarning)


from pandas import Series

chunker=pd.read_csv("C:/Python/pydata/ch06/ex6.csv",chunksize=10)

import sys

import csv

import json

from lxml.html import parse

f=open("C:/Python/pydata/ch06/ex7.csv")


class my_dialect(csv.Dialect):
    lineterminator='\n'
    delimiter=';'
    quotechar='"'

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'http://stackoverflow.com/questions/30519487/pandas-error-invalid-value-encountered
'http://stackoverflow.com/questions/2792650/python3-error-import-error-no-module-name-urllib2

reader=csv.reader(f,dialect=my_dialect)
obj = """
{"name": "Wes",
"places_lived": ["United States", "Spain", "Germany"],
"pet": null,
"siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
{"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''



from urllib.request import urlopen

parsed=parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))


doc=parsed.getroot()

links=doc.findall('.//a')

lnk=links[28]
lnk.get('href')

urls=[lnk.get('href') for lnk in doc.findall('.//a')]

urls[-10:]