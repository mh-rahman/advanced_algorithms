#! /usr/bin/python

import heapq

class myGraph:
    def __init__(self):
        self.nodes={}
    def addNode(self,node,neighbour=None):
        neighbour_list=self.nodes.setdefault(node,[])
        neighbour_list.append(neighbour)
        self.nodes[node]=neighbour_list

class myNode:
    def __init__(self,id,edges=None,weights=0):
        self.id=id
        self.weights={}
        self.parent=None
        self.dist=100000
        self.explored=0
    #def __lt__():

def initialization(file_name):
    with open(file_name) as f:
        graph_=[line.split() for line in f]

    i=-1

    for l in graph_:
        i+=1
        nodes.append(int(l[0]))
        edges.append([])
        weights.append([])
        for j in range(1,len(l)):
            x,y=l[j].split(',')
            edges[i].append(int(x))
            weights[i].append(int(y))
        #myGraph.append(nodeClass(nodes,edges,weights))    

    #Using objects:
    # myGraph=[]
    # for l in graph_:
    #     i+=1
    #     node=int(l[0])
    #     edges=[]
    #     weights=[]
    #     for j in range(1,len(l)):
    #         x,y=l[j].split(',')
    #         edges.append(int(x))
    #         weights.append(int(y))
    #     myGraph.append(nodeClass(node,edges,weights))
    # return myGraph

def djikstraMethod(n):
    ind=n-1
    path=[None]*len(nodes)
    dist=[100000]*len(nodes)
    path[ind]=nodes[ind]
    dist[ind]=0
    node_heap=[(x,y) for x,y in zip(dist,nodes)]
    heapq.heapify(node_heap)
    while node_heap:
        curr=heapq.heappop(node_heap)
        curr_ind=curr[1]-1
        isExplored[curr_ind]=1
        for i in range(len(edges[curr_ind])):
            e=edges[curr_ind][i]
            if isExplored[e-1]:
                continue
            if dist[e-1]>dist[curr_ind]+weights[curr_ind][i]:
                dist[e-1]=dist[curr_ind]+weights[curr_ind][i]
                path[e-1]=curr[1]
        
        while node_heap:
            heapq.heappop(node_heap)
        
        node_heap=[(x,y) for x,y,z in zip(dist,nodes,isExplored) if z==0]
        heapq.heapify(node_heap)

    return path,dist


nodes=[]
edges=[]
weights=[]
#file_name='input_random_1_4.txt'
file_name='dijkstraData.txt'
initialization(file_name)
res=[7,37,59,82,99,115,133,165,188,197]
isExplored=[0]*len(nodes)
path,dist=djikstraMethod(1)
for x,y in zip(nodes,dist):
    print(x,' : ',y)
reachable=[dist[x-1] for x in res]
print(reachable)

# OOP approach:
# myGraph=initialization()
# print(len(myGraph))
# print(myGraph[0] < myGraph[1])


