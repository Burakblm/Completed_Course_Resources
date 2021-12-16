# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:05:16 2021

@author: ASUS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler = pd.read_csv("sepet.csv", header=None)

t = []
for i in range(0,7501):
    t.append([str(veriler.values[i,j]) for j in range(0,20)])

from apyori import apriori

kurallar = apriori(t, min_support= 0.01,min_confidence=0.2,min_lift=3)

print(list(kurallar))


