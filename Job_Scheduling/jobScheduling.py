#! /usr/bin/python

def keyFunc(weight, length):
    #return weight-length
    return weight/length

class job:
    def __init__(self, weight, length):
        self.weight=weight
        self.length=length
        self.key=keyFunc(weight,length)
        #print('Job: ', self.weight, self.length, self.key)

    def __lt__(self, job2):
        if self.key!=job2.key:
            return self.key< job2.key
        else:
            return self.weight < job2.weight
        



def scheduler(jobs):
    jobs.sort()
    jobs.reverse()
    weighted_completion_time=0
    t=0
    for j in jobs:
        t+=j.length
        weighted_completion_time+=j.weight*t
    return weighted_completion_time


#fileName='input_random_7_20.txt'
fileName='jobs.txt'

with open(fileName) as f:
    #jobs=[job(int(x.split()[0]),int(x.split()[1])) for x in f]
    n_jobs=f.readline()
    jobs=[job(int(x.split()[0]),int(x.split()[1])) for x in f]



weighted_completion_time=scheduler(jobs)
print(weighted_completion_time)

# jobs.sort()
# jobs.reverse()
# print('After Sort:')
# for j in jobs:
#     print(j.key, j.weight, j.length)

# test=job(3,2)
# print(test.key)