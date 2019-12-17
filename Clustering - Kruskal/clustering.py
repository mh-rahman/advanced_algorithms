#!/usr/bin/python

class unionFind():
    componentDict = {}
    clusters = {}
    size = {}

    def __init__(self,nodeSet):
        self.componentDict = {x:x for x in nodeSet}
        self.clusters = {x:[x] for x in nodeSet}
        self.size = {x:1 for x in nodeSet}
    
    def union(self,u,v):
        c1 = self.componentDict[u]
        # print('C1:',c1)
        # print(self.clusters[c1])
        c2 = self.componentDict[v]
        # print('C2:',c2)
        # print(self.clusters[c2])
        if self.size[c1] > self.size[c2]:
            # self.componentDict[v] = c1
            for x in self.clusters[c2]:
                self.componentDict[x] = c1
                self.clusters[c1].append(x)
            self.size[c1]+=self.size[c2]
            self.size.pop(c2)
            self.clusters.pop(c2)
        else:
            # print('In else')
            for x in self.clusters[c1]:
                self.componentDict[x] = c2
                self.clusters[c2].append(x)
            self.size[c2]+=self.size[c1]
            self.size.pop(c1)
            self.clusters.pop(c1)
        
        return 0

def initialization(fileName):
    with open(fileName) as f:
        num = int(f.readline())
        edges = [[int(x) for x in line.split(' ')] for line in f]
    nodeSet = set([])
    for e in edges:
        nodeSet.add(e[0])
        nodeSet.add(e[1])
    edges.sort(key=lambda edge: edge[2])

    return nodeSet, edges, num

def kruskals(nodeSet, edges, num):
    uf = unionFind(nodeSet)
    clusterCount = num
    maxSpacing = 0

    while clusterCount >= 4:
        e = edges.pop(0)
        maxSpacing = e[2]
        u = e[0]
        v = e[1]
        if uf.componentDict[u] != uf.componentDict[v]:
            uf.union(u,v)
            clusterCount-=1
    
    return maxSpacing


fileName = 'clustering1.txt'
nodeSet, edges, num = initialization(fileName)
maxSpacing = kruskals(nodeSet, edges, num)
print(maxSpacing)