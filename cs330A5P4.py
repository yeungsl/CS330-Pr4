# -*- coding: utf-8 -*-
"""
cs330
Assigment 5
problem 4

Sailung Yeung
email: yeungsl@bu.edu

Shang-Hung Tsai
email: tsaicash@bu.edu
"""
import matplotlib.pyplot as plt
import random
import numpy as np
import copy
import time
import heapq
##(a)
def findIfPartition(a):
    t = time.clock()
    s = sum(a)
    o = 0
    if s % 2 != 0:
        s -= 1
    sub = np.zeros((s//2 + 1, len(a)+1))
    for i in range(len(a)+1):
        sub[0][i] = 1
        o += 1
    
    r = 0
    for i in range(1, s//2 + 1):
        for j in range(1, len(a)+1):
            sub[i][j] = sub[i][j-1]
            if i >= a[j-1]:
                sub[i][j] = (sub[i][j] or sub[i-a[j-1]][j-1])
         
            ##print(sub)
            if i == s//2 and sub[i][j] == 1:
                r = j
                break
            o += 1
        
    #print(sub)
    #print("r:", r)
    if sum(a[0:r]) == s//2:
        print("A1: ", a[0:r], " A2: ", a[r:],"\n")
    else:
        for i in range(len(a[0:r])):
            o += 1
            d = copy.deepcopy(a[0:r])
            #print("befor",d)
            del d[i]
            #print("after",d)
            if sum(d) == s//2:
                print("A1: ",d," A2: ",a[r:]+[a[i]],"\n" )
                break
    t1 = time.clock() - t
    print("Running time: ", t1,"s")
    print("# of Operation: ", o, " = m * n, where m is the size of the input array and n is the array sum/2")
    return t1

##(b)
def kk(a):
    ##pre-prosessing the list
    ##make all the elements in the list to be negative then put them into a min heap
    ##so that every time it pops a value, it will have the most small value returned
    ##if negated the value poped will become the max value in the list
    t = time.clock()
    o = 0
    na = [x * -1 for x in a]
    ##print(na)
    heapq.heapify(na)
    for i in range(len(na)):
        n1 = heapq.heappop(na) * -1
        n2 = heapq.heappop(na) * -1
        n = n1 - n2
        ##print(n)
        heapq.heappush(na, n * -1)
        heapq.heappush(na, 0)
        ##print(na)
        o += 1
    t1 = time.clock() - t
    print("the residue is: ", (min(na) * -1))
    print("Running time: ", t1,"s")
    
    return t1
    
##(c)
def doC():
    ta = []
    tb = []
    for n in range(3,13):
        ls = [random.randrange(10**n) for i in range(100)]
        #print(ls)
        #ta += [findIfPartition(ls)] ## limitation seems to be 10 ** 4,have to wait so long for 10 ** 5
        tb += [kk(ls)]
    print(tb)
    plt.xlabel("the exponent of 10**(3... 12)")
    plt.ylabel("the total seconds taken by the two process")
    plt.title("the comparison of the running time of the two algorithm")
    plt.plot(tb,'r-')
    plt.legend()
    
    
