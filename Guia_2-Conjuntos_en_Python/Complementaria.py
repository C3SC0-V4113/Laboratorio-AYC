# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 20:19:57 2022

@author: frank
"""

from sympy import FiniteSet,Complement
from sympy.combinatorics import Subset
A=['A','B','C','D','E']
B=['B','D','E']


#Como encontrar subconjuntos(Inclusión)
C=Subset(B,A)

print("Subconjunto: ",C.subset)


#Como se trabaja el complemento del conjuntos


D=Complement(set(A),set(B))
print("Complemento de A con B: ",D)