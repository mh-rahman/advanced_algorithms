#!/usr/bin/python

def getResult(reconstruction):
    toCheck = [1, 2, 3, 4, 17, 117, 517, 997]
    result = [str(reconstruction[i-1]) if i<=len(reconstruction) else '0' for i in toCheck]
    return ''.join(result)


# fileName = 'input_random_40_4000.txt'
fileName = 'mwis.txt'
with open(fileName) as f:
    temp = f.readline()
    weights = [int(line) for line in f]

l = len(weights)

opt = [0]*l

opt[0] = weights[0]
opt[1] = max(weights[0], weights[1])

for n in range(l):
    opt[n] = max(opt[n-1], opt[n-2]+weights[n])

reconstruction = [0]*l

i = l-1
# for n in range(l-2,-1,-1):
while i>1: #hs to be 1
    # if opt[i] == opt[i-1]:
    if opt[i] == opt[i-2]+weights[i]:
        reconstruction[i] = 1
        i-=2
    else:
        # print('Here', i)
        reconstruction[i] = 0
        i-=1

reconstruction[1] = 1 if reconstruction[2]!=1 and weights[1]>weights[0] else 0
reconstruction[0] = 0 if reconstruction[1] == 1 else 1

# print(opt)
# print(reconstruction)

print(getResult(reconstruction))

