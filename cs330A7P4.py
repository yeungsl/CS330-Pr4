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
import math
import statistics as st
import pandas as pd

##kk
def kk(a):
    ##pre-prosessing the list
    ##make all the elements in the list to be negative then put them into a min heap
    ##so that every time it pops a value, it will have the most small value returned
    ##if negated the value poped will become the max value in the list
    #startTime = time.clock()
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
        
        
    #runtime = time.clock() - startTime
    #print(na)
#    print("For KK algorithm:")
#    print("The residue is: ", (min(na) * -1))
#    print("Running time: ", runtime,"s")
#    print("number of operation: ", operation)
#    print()
    
    return (min(na) * -1)


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
    

##Simulated Annealing
def sa(a, k):
    length = len(a)
    sign = randoml(length)
    
    currentResidue = abs(residue(a, sign))
    
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
        
        newResidue = abs(residue(a, sign2))
        p = P(newResidue, currentResidue, i)
        j = random.random()
        ##print(p)
        if newResidue < currentResidue:
            sign = sign2
            currentResidue = newResidue
        else:
            if j < p:
                sign = sign2
                currentResidue = newResidue
                
    return currentResidue
    
    
    
def P(rnew, rold, i):
    t = (10**10) * (0.8**math.floor(i/300))
    ##print(t)
    return math.exp(-1*(rnew - rold/t))
    
    
    
    
def test():
    k = []
    r = []
    g = []
    s = []  
    nk = 50
    for i in range(nk):
        ls  = [random.randrange(10**12) for i in range(100)]
        k.append(kk(ls))
        r.append(rr(ls, 25000))
        g.append(gd(ls, 25000))
        s.append(sa(ls, 25000))
    print("kk",st.mean(k))
    print("rr", st.mean(r))
    print("gd", st.mean(g))
    print("sa", st.mean(s))
    
    plt.xlabel("number of instances")
    plt.ylabel("residue")
    plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])
    x = np.arange(nk)
    plt.plot(x, k)
    plt.plot(x, r)
    plt.plot(x, g)
    plt.plot(x, s)

    plt.legend(['kk', 'rr', 'gd', 'sa'], loc='upper right')

    plt.show()
    df = pd.DataFrame({"kk":k, "rr":r, "gd":g, "sa":s})
    writer = pd.ExcelWriter("out.xlsx", engine = 'xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    