# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:14:42 2021

@author: ASUS
"""

oku = open("C:\\Users\\ASUS\\Desktop\\Restaurant_Reviews.txt")
yaz = open("yeni_veri.txt","w")

def ilk_virgül_sil(word):
    kelime = ""
    a = word.split(",")
    lenght = len(a)
    for i in range(lenght-1):
        kelime = kelime + "" + a[i]
    
    return kelime +","+ a[len(a)-1]
for i in range(1001):
    yeni_kelime = ilk_virgül_sil(oku.readline())
    yaz.write(yeni_kelime)
print(yeni_kelime)
oku.close()
yaz.close()
    


    
    
    


    
    
    
    
    
    
    
    
