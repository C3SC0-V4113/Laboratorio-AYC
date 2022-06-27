# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:41:36 2022

@author: frank
"""

from sympy import FiniteSet

A=FiniteSet(1,2,3,4,5)
B=FiniteSet(3,4,8,6,0)
PCartesiano=(A*B)
print(PCartesiano)

#Calculando producto cartesiano:
for elemento in PCartesiano:
    print(elemento)