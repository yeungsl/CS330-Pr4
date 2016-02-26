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
import math


# main MST functions
    
def MST(g, test = 1):
    indexList = [0]
    value = 0
    counter = len(g)-1
    
    currentMinList = initCurrentMins(g)
    currentMinList = updateMinList(g, currentMinList, indexList)
    while counter != 0:

        nextMin = findNextMin(currentMinList, indexList)
        nextIndex = nextMin[2]
        removeEdge(g, indexList, nextIndex)
        indexList += [nextIndex]
        
        if (test == 2):
            value += math.sqrt(nextMin[0])        
        else:
            value += nextMin[0]
        
        currentMinList = updateMinList(g, currentMinList, indexList)
        
        counter -= 1

    return value
        
def initCurrentMins(g):
    '''
    This helper function returns a list that contains the 
    current mins of all rows.
    '''        
    currentMinList = []
    for row in range (len(g)):
        currentMinList += [(min(g[row]), row, np.argmin(g[row]))]
    return currentMinList
    
def updateMinList(g, currentMinList, indexList):
    '''
    This helper function updates currentMinList.
    '''
    lastIndex = indexList[-1]
    currentMinList[lastIndex] = (min(g[lastIndex]), lastIndex, np.argmin(g[lastIndex]))
    
    for i in range(len(currentMinList)):
        if (currentMinList[i][2] == lastIndex):
            currentMinList[i] = (min(g[i]), i, np.argmin(g[i]))
            
    return currentMinList
            
        
def findNextMin(currentMinList,indexList):
    '''
    This helper function finds the min in currentMinList 
    that is reachable from the nodes in the index list,
    '''
    reachable = []
    for row in indexList:
        # create a tuple that contains the min value, row, column
        reachable += [currentMinList[row]]

    return min(reachable)
        
def removeEdge(g, indexList, i):
    '''
    This helper function takes a graph, a list, and a index.
    It remove all the edges that connects node i to the nodes in the list.
    '''    
    for j in indexList:
        g[i][j] = 2
        g[j][i] = 2


# part 1
def create1(n):
    '''
    This function initializes the adjacency matrix
    '''
    graph = np.random.random_sample((n,n))
    graph = np.triu(graph,1)  
    graph2 = np.transpose(graph)
    final = graph + graph2
    np.fill_diagonal(final, 2)
    
    return final
    
def doTest1(n):
    g = create1(n)
    return MST(g)


# part 2
def create2(n):
    
    # x and y contains the coordinates of the nodes
    x = np.random.random_sample((1,n))[0]
    y = np.random.random_sample((1,n))[0]

    graph = np.zeros((n,n))
    
    # calculate the distance between two nodes
    for i in range(n):
        for j in range(i):
            graph[i][j] = (x[i]-x[j])**2 + (y[i]-y[j])**2
    
    graph2 = np.transpose(graph)
    final = graph + graph2
    np.fill_diagonal(final, 2)
    return final       

def doTest2(n):
    g = create2(n)
    return MST(g,test=2)

def run(n, test=1):
    total = 0
    
    if test == 2:
        for i in range(5):
            total += doTest2(n)
    else:
        for i in range(5):
            total += doTest1(n)
            
    return total/5
    