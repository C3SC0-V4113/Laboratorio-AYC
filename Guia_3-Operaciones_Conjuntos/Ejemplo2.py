# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:14:49 2022

@author: frank
"""

from sympy import FiniteSet

A=FiniteSet(1,2,3,4)
Potencia=A**2
print("\nSegunda Potencia")
print(Potencia)

for x in Potencia:
    print(x)

#Si queremos calcular la tercera potencia
Potencia2=A**3
print("\nTercera Potencia")
print(Potencia2)

for elemento in Potencia2:
    print(elemento)