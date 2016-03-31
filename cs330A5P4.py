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
def algorithm1(a):
    
    print("For algorithm 1:")
    
    startTime = time.clock() 
    s = sum(a)
    operation = 0  # counter for operation
    
    # handle odd sum
    if s % 2 != 0:
        s -= 1
    
    # initialize 2d array with all 0s    
    sub = np.zeros((s//2 + 1, len(a)+1))
    for i in range(len(a)+1):
        sub[0][i] = 1
        operation += 1
     
    r = 0    # r is the break point in the array
    residue = "xxx"
    
    for i in range(1, s//2 + 1):
        for j in range(1, len(a)+1):
            sub[i][j] = sub[i][j-1]
            if i >= a[j-1]:
                sub[i][j] = (sub[i][j] or sub[i-a[j-1]][j-1])
         
            ##print(sub)
            if i == s//2 and sub[i][j] == 1:
                r = j
                break
            operation += 1
        
    print(sub)
    print("r:", r)
    if sum(a[0:r]) == s//2:
        print("A1: ", a[0:r], " A2: ", a[r:],"\n")
        residue = sum(a[0:r])-sum(a[r:])
        
    else:
        for i in range(len(a[0:r])):
            operation += 1
            d = copy.deepcopy(a[0:r])
            del d[i]
            if sum(d) == s//2:
                print("A1: ",d," A2: ",a[r:]+[a[i]],"\n" )
                residue = sum(d)-sum(a[r:]+[a[i]])
                break
                
#            for j in range(len(a[0:r])):
#                operation += 1
#                
#                #print("befor",d)
#                del d[j]
#                #print("after",d)
#                if sum(d) == s//2:
#                    print("A1: ",d," A2: ",a[r:]+[a[i],a[j]],"\n" )
#                    residue = sum(d)-sum(a[r:]+[a[i]])
#                    break break
#                
#                for k in range(len(a[0:r])):
#                    operation += 1
#                    del d[k]
#                    if sum(d) == s//2:
#                        print("A1: ",d," A2: ",a[r:]+[a[i],a[j],a[k]],"\n" )
#                        residue = sum(d)-sum(a[r:]+[a[i]])
#                        break break break
            
    runtime = time.clock() - startTime
    print("The residue is: ",residue)
    print("Running time: ", runtime,"s")
    print("# of Operation: ", operation, " = m * n, where m is the size of the input array and n is the array sum/2")
    print()
    return runtime

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
    for n in range(3,5):
        ls = [random.randrange(10**n) for i in range(100)]
        print("Input range is 10**"+str(n))
        #print(ls)
        testA += [algorithm1(ls)] ## limitation seems to be 10 ** 4,have to wait so long for 10 ** 5
        testB += [kk(ls)]
    #print(testB)
    
    plt.xlabel("the exponent of 10**(3... 12)")
    plt.ylabel("the total seconds taken by the two process")
    plt.title("the comparison of the running time of the two algorithm")
    plt.plot(testB,'r-')
    plt.legend()
    
    
