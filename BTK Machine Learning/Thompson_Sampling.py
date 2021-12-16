# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:09:24 2021

@author: ASUS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import random

# Random Selection (Rastgele seçim )

veriler = pd.read_csv("Ads_CTR_Optimisation.csv")


N = 10000 # 10000 tıklma 
d = 10 # toplma 10 ilan var 
secilenler = []  
toplam = 0
birler = [0] * d
sifirler = [0] * d


for n in range(1,N):
    ad = 0 # secilen ilan
    max_th = 0
    for i in range(0,d):
        rasbeta = random.betavariate(birler[i] +1 , sifirler[i] +1 )
        
        if(rasbeta > max_th):
            max_th = rasbeta
            ad = i
    secilenler.append(ad)
    odul = veriler.values[n,ad]
    
    if(odul == 1):
        birler[ad] = birler[ad] +1
    else:
        sifirler[ad] = sifirler[ad] + 1
    toplam = toplam + odul
        
print("Toplam ödül : ", toplam)
plt.hist(secilenler)
plt.show()
    
        

