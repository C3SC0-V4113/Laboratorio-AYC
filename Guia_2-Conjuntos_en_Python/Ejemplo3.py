# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 23:32:15 2022

@author: frank
"""

A=[1,9,8,12,24,23,0]
A=set(A)

#Comprobando membresía, es decir, si un elemento pertenece al conjunto:
print("La cardinalidad del conjunto es: ",len(A))
if 12 in A:
    print("True")
    
#Comprobando la igualdad de conjuntos
B=[6,9,8,21,7]
B=set(B)

if A==B:
    print("True")
else:
    print("False")