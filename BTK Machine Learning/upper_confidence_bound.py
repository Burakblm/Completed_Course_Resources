# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 22:21:47 2021

@author: ASUS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

# Random Selection (Rastgele seçim )

veriler = pd.read_csv("Ads_CTR_Optimisation.csv")
'''
import random



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
'''

N = 10000 # 10000 tıklma 
d = 10 # toplma 10 ilan var 
# Ri(n)
oduller = [0] * d # ilk başta butun ilanların odulu 0
# Ni(n)
tiklamalar = [0] * d # o ana kadarki tiklamalar
secilenler = []  
toplam = 0


for n in range(0,N):
    ad = 0 # secilen ilan
    max_usb = 0
    for i in range(0,d):
        
        if(tiklamalar[i]>0):
            ortalama = oduller[i] / tiklamalar[i]
            delta = math.sqrt(3/2 * math.log(n)/ tiklamalar[i])
            ucb = ortalama + delta
            
        else:
            ucb = N*10
            
        if max_usb < ucb: # max'tan buyuk bir usb çıktı
            max_usb = ucb
            ad = i
    secilenler.append(ad)
    tiklamalar[ad] = tiklamalar[ad] + 1
    odul = veriler.values[n,ad]
    oduller[ad] = oduller[ad] + odul
    toplam = toplam + odul
    
print("toplam odul : ",toplam)

plt.hist(secilenler)
plt.show()
















    
    



