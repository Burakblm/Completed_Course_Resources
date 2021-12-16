# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:21:47 2021

@author: ASUS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

veriler = pd.read_csv("Ads_CTR_Optimisation.csv")

N = 10000
d = 10
toplam = 0
secilenler = []

for n in range(0,N):
    ad = random.randrange(d)
    secilenler.append(ad)
    odul = veriler.values[n,ad]
    toplam = toplam + odul
    
    
plt.hist(secilenler)
plt.show()
    
    
    



