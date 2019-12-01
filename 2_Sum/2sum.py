#! /usr/bin/python

import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)


def main():
    
    file_name='2sum.txt'
    with open(file_name) as f:
        numbers=[int(x) for x in f]

    count=0
    num_dict=set()
    for x in numbers:
        num_dict.add(x)
    for target in range(-10000,10001):
        if target%500==0:
            print('Current target = ', target)
        # isPossible=0
        # number_dict={}
        for x in numbers:
            # if num_count%10000==0:
            #     print('Current target = ', target, 'Current number = ', num_count)
            #     num_count+=1
            y=target-x
            # isPossible=number_dict.get(y,0)
            if y in num_dict and y!=x:
            # if isPossible==1:
                count+=1
                break
            # else:
            #     number_dict[x]=1

    print(count)

thread = threading.Thread(target=main)
thread.start()