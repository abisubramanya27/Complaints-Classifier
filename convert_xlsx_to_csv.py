# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 15:50:36 2019

@author: HP
"""
import pandas as pd
import numpy as np
import string
df=pd.read_excel('C:\\Users\\HP\\Documents\\random stuff sem III\\DBS pshift\\smalldata.xlsx')
len = df.shape[0]
print(len)
import re
for i in range(len):
    s = df.iloc[i]['consumer_comp']
    s = re.sub(r'[^\w\s]','',s)
    df.iloc[i]['consumer_comp'] = s;
for i in range(5):
    print(df.iloc[i]['consumer_comp'])
df.to_csv('C:\\Users\\HP\\Documents\\random stuff sem III\\DBS pshift\\small.csv')