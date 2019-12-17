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
        if c1 == c2:
            return 0
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

def bitToInt(x, nBits):
    pow = nBits-1
    sum = 0
    for bit in x:
        if bit == '1':
            sum+=(2**pow)
        pow-=1
    return sum

def initialization(fileName):
    with open(fileName) as f:
        firstLine = f.readline().split(' ')
        # k = int(firstLine[0])
        nBits = int(firstLine[1])
        nodes = [bitToInt(''.join([line[2*x] for x in range(nBits)]), nBits) for line in f]
    return nBits,nodes

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


fileName = 'input_random_40_256_20.txt'
# fileName = 'clustering_big.txt'

nBits,nodes = initialization(fileName)
# print(nodes)
nodeSet = set(nodes)
uf = unionFind(nodeSet)

for u in nodeSet.copy():
    # print(u)
    if u not in nodeSet:
        continue
    nodeSet.remove(u)
    x1 = ''.join(['0']*(nBits-1)+['1'])
    x1 = bitToInt(x1, nBits)

    for i in range(nBits):
        temp = x1^u
        if temp in nodeSet:
            # print("Here")
            # nodeSet.remove(temp)
            uf.union(temp,u)
        x1 = x1 << 1

    x2 = ''.join(['0']*(nBits-1)+['1'])
    x2 = bitToInt(x2, nBits)
    count = 0
    for i in range(nBits):
        x1 = ''.join(['0']*(nBits-1)+['1'])
        x1 = bitToInt(x1, nBits)

        for j in range(nBits):
            if x1 != x2:
                count+=1
                temp = x1^u
                temp = temp^x2
                if temp in nodeSet:
                    # print(u,temp,'here')
                    # print(uf.clusters)
                    # print("Found")
                    # nodeSet.remove(temp)
                    uf.union(temp,u)
            x1 = x1 << 1
        x2 = x2 << 1


clusterCount = len(uf.clusters)
print(clusterCount)
# print(uf.clusters)

