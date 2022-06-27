# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 19:55:16 2022

@author: frank
"""

import imp
from sympy import FiniteSet,subsets
from matplotlib import pyplot as plt
from matplotlib_venn import venn2

A=FiniteSet(1,3,5,7)
B=FiniteSet(1,2,3,4)

v=venn2(subsets=[A,B],set_labels=("A","B"))
v.get_label_by_id('10').set_text(A-B)
v.get_label_by_id('11').set_text(A.intersection(B))
v.get_label_by_id('01').set_text(B-A)
plt.show()