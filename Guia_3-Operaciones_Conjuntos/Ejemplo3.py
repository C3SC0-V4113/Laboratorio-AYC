# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:54:16 2022

@author: frank
"""
import imp
from sympy import FiniteSet
#Dibujando el diagrama de venn de 2 conjuntos
import numpy as np
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

venn2((1,1,1))
plt.show()