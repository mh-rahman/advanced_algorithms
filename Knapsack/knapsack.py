#!/usr/bin/python
from math import gcd
from functools import reduce
import sys
sys.setrecursionlimit(8000)

fileName = 'knapsack_big.txt'
# fileName = 'input_random_40_1000000_2000.txt'
# fileName = 'input_random_24_1000_100.txt'
with open(fileName) as f:
    capacity, numItems = [int(x) for x in f.readline().split(' ')]
    items = [line.split(' ') for line in f]

values = [int(x[0]) for x in items]
weights = [int(x[1]) for x in items]

# print(values)
# print(weights)

n = numItems
m = capacity


#Space efficient iterative
opt1 = [0] * (m+1)
opt0 = [0] * (m+1)
for i in range(0,n+1):
    if i%100 == 0:
        print(i)
    opt0 = opt1.copy()
    for j in range (0,m+1):
        if j==0:
            opt1[j]=0
        elif j>=(weights[i-1]):
            opt1[j]=max(opt0[j],values[i-1]+opt0[j-weights[i-1]])
        else:
            opt1[j]=opt0[j]
# print(opt)
print(opt0[m])
print(opt1[m])

'''#Iterative
for i in range(0,n+1):
    for j in range (0,m+1):
        if i==0 or j==0:
            opt[i][j]=0
        elif j>=(weights[i-1]):
            opt[i][j]=max(opt[i-1][j],values[i-1]+opt[i-1][j-weights[i-1]])
        else:
            opt[i][j]=opt[i-1][j]
# print(opt)
print(opt[n][m])'''

resultDict = {}
# Recursive approach
def getOpt(i,j):
    if resultDict.get((i,j),None) != None:
        return resultDict.get((i,j),None)
    elif i==0 or j==0:
        resultDict[(i,j)] = 0
        return 0
    elif j>=weights[i-1]:
        temp = max(getOpt(i-1,j),values[i-1]+getOpt(i-1,j-weights[i-1]))
        resultDict[(i,j)] = temp
        return temp
    else:
        resultDict[(i,j)] = getOpt(i-1,j)
        return resultDict[(i,j)]

# print(getOpt(n,m))
