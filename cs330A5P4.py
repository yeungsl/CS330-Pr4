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
import time
import heapq
##(a)
def algorithm1(a):
    
    print("For algorithm 1: ")
    start = time.clock()
    operation = 0
    
    s = sum(a)
    if s % 2 != 0:
        s -= 1
    halfs = s//2
    
    # create table
    table = np.zeros((halfs+1, len(a)+1))
    
    for i in range(1, halfs+1):
        for j in range(1, len(a)+1):
            include = table[i-a[j-1]][j-1]+a[j-1]
            if (include <=i and i-(include)<i-table[i][j-1]):
                # if include this element makes the result closer to the sum
                table[i][j] = include
            else:
                # else, we do not include this element
                table[i][j] = table[i][j-1]
            operation += 1
            
    # back track partition
    partition1 = []
    i = halfs
    j = len(a)
    while i != 0 and j != 0:
        for index in range(j+1):
            operation += 1
            if table[i][index] == i:
                partition1 += [index]
                i = int(table[i][index] - a[index-1])
                j -= 1
                break
    
    sign = [1 for x in range(len(a))]
    partition1sum = 0
    
    for i in partition1:
        sign[i-1] *= -1
        partition1sum += a[i-1]
        operation += 1
    print("This is the sign array: ", sign)
 
    partition2sum = sum(a) - partition1sum
    residue = abs(partition1sum - partition2sum)
    print("residue = ", residue)
    
    t = time.clock()-start
    print("Running time: ", t,"s")    
    print("# of Operation (roughly): ", operation)

##(b)
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
    
##(c)
def doC():
    testA = []
    testB = []
#    for n in range(3,13):
    for n in range(3,7):
        ls = [random.randrange(10**n) for i in range(100)]
        print("Input range is 10**"+str(n))
        #print(ls)
        testA += [algorithm1(ls)] ## limitation seems to be 10 ** 4,have to wait so long for 10 ** 5
        testB += [kk(ls)]
    
    plt.xlabel("the exponent of 10**(3... 12)")
    plt.ylabel("the total seconds taken by the two process")
    plt.title("the comparison of the running time of the two algorithm")
    plt.plot(testB,'r-')
    plt.legend()
    
    
