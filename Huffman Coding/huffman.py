#!/usr/bin/python
import heapq

def getDepth(root):
    if root == None:
        return 0
    else:
        return min(getDepth(root.left),getDepth(root.right))+1

class node:
    key = None
    left = None
    right = None

    def __init__(self, key):
        self.key = key

fileName = 'input_random_20_160.txt'
# fileName = 'huffman.txt'
with open(fileName) as f:
    weights = [int(line) for line in f]

symbols = [(y, str(x+1)) for (x,y) in zip(range(len(weights)),weights)]
# symbols.sort(key=lambda symbol: symbol[0])
# print(symbols)
least_weight = symbols[0][1]
nodeDict = {x[1]:node(x[1]) for x in symbols}


heapq.heapify(symbols)
n = None
while len(symbols)>1:
    a = heapq.heappop(symbols)
    b = heapq.heappop(symbols)

    name = a[1]+'.'+b[1]
    weight = a[0]+b[0]
    heapq.heappush(symbols,(weight,name))
    n = node(name)
    n.left = nodeDict[a[1]]
    n.right = nodeDict[b[1]]
    nodeDict[name] = n

print(getDepth(n)-1)

# heapq.heappush(symbols,x)

# print(list(nodeDict.values())[4].key)
# print(symbols)