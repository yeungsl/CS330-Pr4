# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 14:50:20 2016

@author: Sailung Yeung and Shang-Hung Tsai
email: yeungsl@bu.edu and tsaicash@bu.edu
cs330 assignment 7 problem 4
"""
import matplotlib.pyplot as plt
import random
import numpy as np
import copy
import time
import heapq

##kk
def kk(a):
    ##pre-prosessing the list
    ##make all the elements in the list to be negative then put them into a min heap
    ##so that every time it pops a value, it will have the most small value returned
    ##if negated the value poped will become the max value in the list
    startTime = time.clock()
    operation = 0      # counter for operation
    
    na = [x * -1 for x in a]
    ##print(na)
    heapq.heapify(na)    # put all elements into the min heap

    for i in range(len(na)):
        n1 = heapq.heappop(na) * -1
        n2 = heapq.heappop(na) * -1
        n = n1 - n2
        ##print(n)
        heapq.heappush(na, n * -1)
        heapq.heappush(na, 0)
        ##print(na)
        operation += 1
        
        
    runtime = time.clock() - startTime
    #print(na)
    print("For KK algorithm:")
    print("The residue is: ", (min(na) * -1))
    print("Running time: ", runtime,"s")
    print("number of operation: ", operation)
    print()
    
    return runtime


def randoml(l):
    ##creating a random array of -1 and 1s
    ls = []
    for i in range(l):
        n = random.randint(0,1)
        if n == 0:
            ls.append(-1)
        else:
            ls.append(1)
    return ls

def residue(array, sign):
    result = 0
    for i in range(len(array)):
            result += sign[i] * array[i]
    return result


#repeated random
def rr(array, k):
    results = []
    
    for i in range(k):
        l = randoml(len(array))

        results.append(abs(residue(array, l)))
        
    return min(results)
    
##Gradient Descent
def gd(array, k):
    length = len(array)
    sign = randoml(length)
    
    currentResidue = abs(residue(array, sign))
    
    for i in range(k):
        indexI = random.randint(0, length-1)
        indexJ = random.randint(0, length-1)
        while indexI == indexJ:
            indexJ = random.randint(0, length-1)
        
        sign2= copy.deepcopy(sign)
        sign2[indexI] *= -1
         
        n = random.randint(0,1)
        if n == 0:
            sign2[indexJ] *= -1
        
        newResidue = abs(residue(array, sign2))
        
        if newResidue < currentResidue:
            sign = sign2
            currentResidue = newResidue
        
    return currentResidue
    
