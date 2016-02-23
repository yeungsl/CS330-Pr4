# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:42:41 2016

@author: Sailung Yeung
email: yeungsl@bu.edu
teammate: Shang-Hung Tsai
email: tsaicash@bu.edu
this code is written for the problem 4 in cs330 hw3
this code is for simulating the complete graph for many nodes and use Prim's algorigthm to compute each
MST in every graph
"""
import numpy as np

def create(n):
    sample = np.random.random_sample((n,n))
    graph = np.triu(sample,1)
    graph[graph == 0] = 2
    return graph
    
def MST(g):
    r = len(g)
    l = []
    l[0] = 0
    v = 0
    counter = r
    i = 1
    while counter != 0:
        l[i] = np.argmin(g[i])
        v += g[l[i]]
        i = l[i]
        
def findMin(g,l):
    return np.argwhere(g == min([min(g[x]) for x in l]))
        