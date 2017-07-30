# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
path='C:/Python/pydata//ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records=[json.loads(line) for line in open(path)]
records[0]
records[0]['tz']

time_zones=[rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts


from collections import defaultdict

def top_counts(count_dict, n=10):
    value_key_pairs=[(count,tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
    
from pandas import DataFrame, Series
import pandas as pd
frame=DataFrame(records)

clean_tz=frame['tz'].fillna("Missing")
clean_tz[clean_tz ==' ']='Unknown'
tz_counts=clean_tz.value_counts()
results = Series([x.split()[0] for x in frame.a.dropna()])
cframe=frame[frame.a.notnull()]

import numpy as np
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
import matplotlib.pyplot as plt

by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts=by_tz_os.size().unstack().fillna(0)
indexer=agg_counts.sum(1).argsort()
indexerat=agg_counts.sum(0).argsort()
count_subset = agg_counts.take(indexer)[-10:]