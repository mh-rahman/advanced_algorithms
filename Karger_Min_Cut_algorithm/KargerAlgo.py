#! /usr/bin/python
from random import seed
from random import randint
from copy import deepcopy
from math import log,inf

def contraction(graph,node1,node2):
    if -1 in graph[node1-1] or -1 in graph[node2-1]:
        return
    for i in range (1, len(graph[node2-1])):
        node3=graph[node2-1][i]
        graph[node3-1]=[node1 if x==node2 else x for x in graph[node3-1]]
    graph[node1-1]=graph[node1-1]+graph[node2-1][1:]
    graph[node2-1]=[node2, -1]
    for i in range (1, len(graph[node1-1])):
        if graph[node1-1][i]==node1:
            graph[node1-1][i]=0
    while 0 in graph[node1-1]:
        graph[node1-1].remove(0)

def randomSelector(graph):
    node1=randint(1,len(graph))
    #node2=randint(1,len(graph))
    #node2=2
    #print(node1,node2)
    #while -1 in graph[node1-1] or -1 in graph[node2-1] or node1==node2:
    while -1 in graph[node1-1]:
        node1=randint(1,len(graph))
        #node2=randint(1,len(graph))
        #print(node1,node2)
    node2=graph[node1-1][randint(1,len(graph[node1-1])-1)]
    #print('nodes = ',node1,node2)
    return node1,node2


with open('KargerMinCut.txt') as f:
#with open('input_random_10_25.txt') as f:
    orig_graph=[[int(x) for x in line.split()] for line in f]
#seed(110)
#print(graph)
#contraction(graph,1,2)
min=inf
unchanged_count=0
#graph1=deepcopy(graph)
length=len(orig_graph)
rn=int((length**2)*log(length))
print('iterations =', rn)
for s in range (0,rn):
    seed(s)
    graph=deepcopy(orig_graph)
    for _ in range(len(graph)-2):
        node1,node2=randomSelector(graph)
        contraction(graph,node1,node2)
        #print(graph)
    m=max([len(x)-1 for x in graph])
    if m<min:
        min=m
        print('iteration = ',s,'min = ',min)
        unchanged_count=0
    else:
        unchanged_count+=1
    if(unchanged_count>=100): #If min value not updating then stop after 100 additional iterations
        break;
    #print(m)
    #print('min = ',min)

print('Final min = ',min)
