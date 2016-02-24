# -*- coding: utf-8 -*-
"""
@author: Sailung Yeung
email: yeungsl@bu.edu
teammate: Shang-Hung Tsai
email: tsaicash@bu.edu

This code is written for the problem 4 in cs330 hw3

This code is for simulating the complete graph for many nodes and use 
Prim's algorigthm to compute each MST in every graph
"""
import numpy as np

def create(n):
    '''
    This function initializes the adjacency matrix
    '''
    graph = np.random.random_sample((n,n))
#    graph = np.triu(sample,1)
#    graph[graph == 0] = 2
    for i in range(n):
        for j in range(i):
            graph[i][j] = graph[j][i]
    np.fill_diagonal(graph, 2)
    return graph
    
def MST(g):
    indexList = [0]
    value = 0
    counter = len(g)-1
    
#    print(g)
    while counter != 0:

        nextMin = findMin(g, indexList)
        nextIndex = nextMin[2]
        removeEdge(g, indexList, nextIndex)
        indexList += [nextIndex]
        value += nextMin[0]
        
        counter -= 1
#        print("new graph = \n", g)
#        print("counter = ", counter)
#        print("indexList = ", indexList)
#        print("value = ", value)
#        print()
        
#    print(value)
    print(indexList)
    return value
        
def findMin(g,indexList):
    '''
    This helper function takes a graph and a list,
    it calculates the min for each row in the list,
    and then returns a tuple that contains information about the 
    overall min and its row and column index.
    '''
    minList = []
    for row in indexList:
        # create a tuple that contains the min value, row, column
        minList += [(min(g[row]),row, np.argmin(g[row]))]
    
#    print("this is the minList = ", minList)
    return min(minList)
        
def removeEdge(g, indexList, i):
    '''
    This helper function takes a graph, a list, and a index.
    It remove all the edges that connects node i to the nodes in the list.
    '''    
    for j in indexList:
        g[i][j] = 2
        g[j][i] = 2

def doTest1(n):
    g = create(n)
    return MST(g)









    