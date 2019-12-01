# !/usr/bin/python

from math import inf
import heapq
import random

class node:

    def __init__(self, id, neighbor = None, weight = 0):
        self.id = id
        self.neighbors = {}
        self.dist = inf
        self.parent = None
        self.isExplored = 0
        if neighbor != None:
            self.setNeighbor(neighbor,weight)
        #print('Job: ', self.weight, self.length, self.key)
    
    def __lt__(self, other):
        return self.dist < other.dist
        # if self.key != job2.key:
        #     return self.key< job2.key
        # else:
        #     return self.weight < job2.weight

    def setExplored(self):
        self.isExplored = 1

    def getExplored(self):
        return self.isExplored

    def getID(self):
        return self.id

    def setNeighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight
    
    def getNeighbors(self):
        return self.neighbors

    def getDist(self):
        return self.dist
    
    def setDist(self,newDist):
        self.dist = newDist
    
    def setParent(self,newParent):
        self.parent = newParent
    
    def getParent(self):
        return self.parent

class graph:
    def __init__(self):
        self.nodes = {}
    
    def addEdge(self,t):
        id1,id2, weight = t
        if id1 not in self.nodes.keys():
            node1 = node(id1)
            self.nodes[id1] = node1
        else:
            node1 = self.nodes[id1]
        if id2 not in self.nodes.keys():
            node2 = node(id2)
            self.nodes[id2] = node2
        else:
            node2 = self.nodes[id2]
        node1.setNeighbor(id2,weight)
        node2.setNeighbor(id1,weight)
        
    def getNodes(self):
        return self.nodes



def prims(myGraph,start = 1):
    l = myGraph.getNodes()
    totalWeight=0
    l[start].setDist(0)
    l[start].setParent(None)

    val = list(l.values())
    heapq.heapify(val)
    while val:
        u = heapq.heappop(val)
        totalWeight+=u.getDist()
        u.setExplored()
        adj_list = list(u.neighbors.keys())
        for v in adj_list:
            if l[v].isExplored != 1:
                if l[v].getDist() > u.neighbors[v]:
                    l[v].setDist(u.neighbors[v])
                    l[v].setParent(u.getID())
        heapq.heapify(val)
    parent=[]
    for i in l.keys():
        parent.append((i,l[i].getParent()))
    print(totalWeight)
    #print(parent)
    return 0


#fileName = 'input_random_50_10000.txt'
#fileName='test.txt'
fileName = 'edges.txt'

with open(fileName) as f:
    #jobs = [job(int(x.split()[0]),int(x.split()[1])) for x in f]
    line1 = f.readline().split()
    n_nodes, n_edges = line1[0], line1[1]
    #nodes = [node(int(x.split()[0]),int(x.split()[1]),int(x.split()[2])) for x in f]
    entries = [(int(x.split()[0]),int(x.split()[1]),int(x.split()[2])) for x in f]

# for n in entries:
#     print(n)

myGraph = graph()
for e in entries:
    myGraph.addEdge(e)

prims(myGraph)
