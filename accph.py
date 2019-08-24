# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:21:36 2019

@author: HP
"""
import pandas as pd
def accphmatch(num):
    path='C:\\Users\\HP\\Documents\\random stuff sem III\\DBS pshift\\python scripts\\phno.csv'
    df=pd.read_csv(path)
    len=df.shape[0]
    chk=False
    for i in range(0,len):
        if df.iloc[i]['phone number']==num:
            chk=True
            return('The account number is '+str(df.iloc[i]['account number']))
    if chk==False:
        return('No matches')

#accphmatch(949815146)