# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:59:26 2019

@author: Ami.Munshi
"""

#To implement DCT


import math
N= (input("Enter the order N: "))
C=[]
T=[[0]*N]*N
for v in range(0,N):
    for u in range(0,N):
        if u==0:
            x=float(1./N)
            x1=math.sqrt(x)
            C.append(x1) 
            T[u][v]= x1
        else:
            a= math.sqrt(2./N)
            b= (math.pi*u*(2*v+1))
            c= 2*N
            d=b/c
            e=math.cos(d)
            temp= round(a*e,3)
            C.append(temp)
            T[u][v]= temp
print(T)
