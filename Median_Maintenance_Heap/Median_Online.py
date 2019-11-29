#! /usr/bin/python
import heapq
from copy import deepcopy

fileName='Median.txt'
with open(fileName) as f:
    stream=[int(x) for x in f]

median=[]
curr=[]
counter=0
for i in stream:
    if counter%100==0:
        print(counter)
    counter+=1
    curr.append(i)
    heap_arr=deepcopy(curr)
    l=len(curr)
    if l%2==0:
        median_position=int(l/2)-1
    else:
        median_position=int((l+1)/2)-1
    #print(median_position)
    heapq.heapify(heap_arr)
    if median_position==0:
        temp=heap_arr[0]
    else:
        temp=heapq.nsmallest(median_position+1, heap_arr).pop()
    # for j in range(median_position):
    #     temp=heapq.heappop(heap_arr)
    median.append(temp)

#print(median)
print(sum(median)%10000)