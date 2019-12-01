#! /usr/bin/python

import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

#sys.resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

def main():

    def reverse_graph(nodes,edges):
        length=len(edges)
        rev_graph=[[] for i in range (length)]
        # print(len(rev_graph))
        # print(len(edges))
        for i in range (length):
            if i%1000 ==0:
                print('Reverse graph generation. Current node = ', i)
            for j in edges[i]:
                #print(i,j)
                rev_graph[j-1].append(i+1)
        # rev_graph=[]
        # for i in nodes:
        #     if i%1000 ==0:
        #         print('Reverse graph generation. Current node = ', i)
        #     rev_graph.append([])
        #     for j in range(len(edges)):
        #         if i in edges[j]:
        #             # print(rev_graph,i,j)
        #             rev_graph[i-1].append(j+1)
        return rev_graph

    def dfs(n,counter):
        isExplored[n-1]=1
        # if curr_leader not in leader:
        #     leader.add(curr_leader)
        #print('node = ',n, 'leader = ', curr_leader)
        for e in rev_edges[n-1]:
            if isExplored[e-1]==0:
                #print(counter)
                #counter=dfs(e,curr_leader,counter)
                counter=dfs(e,counter)
        counter+=1
        fin_time[n-1]=counter
        return counter

    def dfsloop():
        counter=0
        #curr_leader=None
        for iter in range(len(nodes)-1,-1,-1):
            if iter%1000==0:
                print('Current iteration in dfsloop = ',iter)
                print('Explored = ', sum(isExplored),'/',len(isExplored))
            # print('iter = ', iter)
            # print('node = ',nodes[iter])
            if isExplored[nodes[iter]-1]==0:
                #curr_leader=nodes[iter]
                #counter=dfs(nodes[iter],curr_leader,counter)
                counter=dfs(nodes[iter],counter)

    def dfs2(n,scc_counter):
        isExplored[n-1]=1
        for e in edges[n-1]:
            if isExplored[e-1]==0:
                scc_counter=dfs2(e,scc_counter)
        scc_counter+=1
        return scc_counter

    def getSCC():
        counter=[]
        for iter in new_nodes:
            if isExplored[iter-1]==1:
                continue
            scc_counter=1
            isExplored[iter-1]=1
            for e in edges[iter-1]:
                if isExplored[e-1]==0:
                    scc_counter=dfs2(e,scc_counter)
            counter.append(scc_counter)
        return counter


    #using dict of {finisht_time:index}, sort by dec order of keys i.e. finish_time to process in order of finish time in second pass

    #with open('input_mostlyCycles_68_320000.txt') as f:
    #with open('test.txt') as f:
    with open('SCC.txt') as f:
        graph_=[[int(x) for x in line.split()] for line in f]

    #print(graph_)
    nodes=[]

    #nodes=[-1 if l[0] in nodes else l[0] for l in graph_]
    prev=-1
    for l in graph_:
        # if l[0] not in nodes:
        #     nodes.append(l[0])
        if l[0]!=prev:
            prev=l[0]
            nodes.append(l[0])
    #print(nodes)
    print('hello1')
    print(len(nodes))

    if len(nodes)<max(nodes):
        nodes=[i for i in range (1,max(nodes)+1)]
    #print(nodes)
    print('hello2')

    edges=[set() for i in range (len(nodes))]
    #print(edges)
    print('hello3')

    for l in graph_:
        edges[l[0]-1].add(l[1])
        #print(edges)
    #print(edges)
    print('hello4')

    n=len(nodes)
    fin_time=[0]*n
    isExplored=[0]*n

    # print('Explored:')
    # print(isExplored)
    print('hello5')

    rev_edges=reverse_graph(nodes,edges)
    print('Reverse Edges computed.')
    print('Number of nodes = ', len(nodes))
    print('Explored = ', sum(isExplored),'/',len(isExplored))
    #print(rev_edges)

    #First pass
    dfsloop()
    print('First pass completed')
    #leader.remove(-1)

    # print('Explored:')
    # print(isExplored)
    # print('finish_times:')
    # print(fin_time)
    # print(nodes)

    #reset explored to 0

    isExplored=[0]*n

    node_dict={fin_time[i]:nodes[i] for i in range(n)}

    #print(node_dict)

    fin_time.sort()
    fin_time.reverse()
    print('Reversed finish time list.')
    # print(fin_time)

    new_nodes=[node_dict[x] for x in fin_time]
    # dfsloop(edges)
    # print(nodes)

    # print("Creating unique leaders list. ",len(leader))
    # leader_unique=[x for x in new_nodes if x in leader]
    # print("Created unique leaders list. ",len(leader_unique))
    # print(leader_unique)

    # leader=set([-1])

    print('Starting SCC counter method.')
    scc_counter_arr=getSCC()
    print('Finished SCC counter method.')
    # print('leaders:')
    # print(leader)
    #print(scc_counter_arr)
    print(sum(scc_counter_arr))

    max_array=[0]*5
    scc_counter_arr.sort()
    scc_counter_arr.reverse()
    n_scc=len(scc_counter_arr)
    max_array[:min(5,n_scc)]=scc_counter_arr[:min(5,n_scc)]
    print(max_array)


thread = threading.Thread(target=main)
thread.start()
