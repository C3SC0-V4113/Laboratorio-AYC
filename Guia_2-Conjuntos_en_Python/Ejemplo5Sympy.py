# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 00:12:50 2022

@author: frank
"""

from sympy import FiniteSet
C=FiniteSet(1,2,3)
print("Utilizando FiniteSet: ",C)

#Generando el conjunto potencia
#Solo se puede hacer con FiniteSet
Potencia=C.powerset()
print("Conjunto Potencia: ",Potencia)

#Cardinalidad:
print("La cardinalidad del conjunto potencia es: ",len(C.powerset()))

#Igualdad
A=FiniteSet("x","w","z","k")
B=FiniteSet("x","c","t")
if A==B:
    print("True")
else:
    print("False")
    
#Unión de dos conjuntos:
UnionConjuntos=A.union(B)
print("Unión de conjuntos con FiniteSet: ",UnionConjuntos)

#Intersección de conjuntos:
Interseccion=A.intersection(B)
print("Intersección de conjuntos con FiniteSet: ",Interseccion)

#Diferencia
Diferencia=A-B
print("Diferencia de conjuntos con FiniteSet: ",Diferencia)