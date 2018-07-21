# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 11:49:07 2018

@author: vibhanshu.singh
"""


import numpy as np
stories=100
B = np.zeros(stories+1)
n = range(stories+1)

for i in range(2, len(B)):
    print ("B["+str(i-1)+"] = "+str(B[i-1]))
    n_list = []
    for j in range(1, i+1):
        n_list+=[max(j, 1+B[i-j])]
    B[i] = min(n_list)
