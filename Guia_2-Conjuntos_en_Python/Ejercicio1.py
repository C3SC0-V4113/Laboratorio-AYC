# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:36:44 2022

@author: frank
"""

from sympy import FiniteSet
A=FiniteSet('A','B','C','D','E')
B=FiniteSet('B','D','E')

#Union de A con B
UnionAB=A.union(B)
print("Unión de conjuntos con FiniteSet: ",UnionAB)

#Intersección entre si mismo
IntersecBB=B.intersect(B)
print("Intersección de conjuntos con FiniteSet: ",IntersecBB)

#Resta de B con A
SubsBA=B-A
print("Diferencia de conjuntos con FiniteSet: ",SubsBA)

#Conjunto Potencia de A
PotenciaA=A.powerset()
print("Conjunto Potencia: ",PotenciaA)

#Cardinal del conjunto potencia de A
print("La cardinalidad del Conjunto Potencia de A es: ",len(PotenciaA))