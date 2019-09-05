# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:53:09 2019

@author: HP
"""
import tarfile
name='C:\\Users\\HP\\Documents\\random stuff sem III\\DBS pshift\\output.tar.gz'
tar=tarfile.open(name, mode='r', fileobj=None)
tar.list();
tar.extractall()

import json
with open('predictions.jsonl') as f:
       for line in f:
           data=json.loads(line)
           print(data['Classes'][0])