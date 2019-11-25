def partition(int_list,l,r,p):
    #print(l,r,int_list)
    #FIND PIVOT AND SWAP WITH FIRST ELEMENT (L)
    int_list[p],int_list[l]=int_list[l],int_list[p]
    p=l
    explorer=l+1
    pointer=l
    pivot=int_list[p]
    while explorer<r+1:
        if explorer == p: #unnecessary since pivot is now at l
            continue
        elif int_list[explorer]>int_list[p]:
            explorer+=1
        elif int_list[explorer]<int_list[p]:
            pointer+=1
            int_list[explorer],int_list[pointer]=int_list[pointer],int_list[explorer]
            explorer+=1
    int_list[pointer],int_list[p]=int_list[p],int_list[pointer]
    p=pointer

    return p

def median(int_list,l,r):
    length=r-l+1
    if length%2==0:
        mid=l+(length//2)-1
    else:
        mid=l+length//2
    if int_list[l]!=max(int_list[l],int_list[r],int_list[mid]) and int_list[l]!=min(int_list[l],int_list[r],int_list[mid]):
        return l
    elif int_list[r]!=max(int_list[l],int_list[r],int_list[mid]) and int_list[r]!=min(int_list[l],int_list[r],int_list[mid]):
        return r
    else:
        return mid

def quickSort(int_list,l,r):
    count=0
    if l>=r:
        return count

    #pivot=int_list[l]
    #Setting first element in array as pivot
    #p=l
    #Setting last element in array as pivot
    #p=r
    #setting median of first, last and middle element as pivot
    p=median(int_list,l,r)

    np=partition(int_list,l,r,p)
    count=r-l
    count1=quickSort(int_list,l,np-1)
    count2=quickSort(int_list,np+1,r)
    count=count+count1+count2
    return count

#int_list=[3, 2, 10, 6, 7, 1, 9, 5, 4, 8]
#int_list=[4,3,2,5,1]
#int_list=[3,2,1,4,5]
#int_list=[]
# p=median(int_list,0,len(int_list)-1)
# print(p)
#count=quickSort(int_list,0,len(int_list)-1)
#print(int_list)
#print(count)

with open('QuickSort.txt') as f:
    int_list=[int(x) for x in f]
    count=quickSort(int_list,0,len(int_list)-1)
    # p=median(int_list,0,len(int_list)-1)
    # print(p)
    print(count)
