# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 17:09:17 2021

@author: ASUS
"""

import random
import pandas as pd

data = pd.read_csv("C:\\Users\\ASUS\\Desktop\\yazdır.csv")

data2 = data["words"].values
print(data.shape)

for i in range(10):
    sayı = random.randint(0,20000)
    print(data2[sayı])
    
    
    