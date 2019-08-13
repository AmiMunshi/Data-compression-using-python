# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:29:32 2019

@author: Ami.Munshi
"""
## To implement Golomb code

def unary1(N):
    N= int(N)
    A= []
    for i in range(N):
        A.append(1)
    A.append(0)
    B= [str(k) for k in A]
    C= "".join(B)
    return(C)

import math
m= input("Enter m ")
n= input("Enter n ")
q= n/m
code1= unary1(q)
k= int(round(math.log(m,2)))
c= 2**k -m
r= n%m
if r<c:
    code2= format(r, '08b')[-(k-1)::]
    
else:
    code2= format(r+c, '08b')[-k::]
code=code1+code2
print("Golomb code is ",code)