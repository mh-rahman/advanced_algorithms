def merge_count(list1,list2,length1,length2):
  int_list=[]
  count=0
  i1=0
  i2=0
  while i1<length1 and i2<length2:
    if list1[i1]<=list2[i2]:
      int_list.append(list1[i1])
      i1+=1
    else:
      int_list.append(list2[i2])
      count+=(length1-i1)
      i2+=1
  if i1<length1:
    while i1<length1:
      int_list.append(list1[i1])
      i1+=1
  if i2<length2:
    while i2<length2:
      int_list.append(list2[i2])
      i2+=1
  return count,int_list

def count_inversion(int_list,length):
  count=0
  if length==1:
    return count,int_list
  else:
    list1=int_list[:length//2]
    list2=int_list[length//2:]
    count1,list1=count_inversion(list1,length//2)
    count2,list2=count_inversion(list2,length-length//2)
    count_merge,int_list=merge_count(list1,list2,length//2,length-length//2)
    count=count1+count2+count_merge
  return count,int_list

def alg(path):
    file=open(path,"r")
    int_list=file.read()
    length=len(int_list)
    count,int_list=count_inversion(int_list,length)
    return count


#file=open("Counting_Inversions_IntegerArray.txt","r")
#int_list=file.read()
with open('Counting_Inversions_IntegerArray.txt') as f:
    int_list=[int(x) for x in f]
#print(int_list)
#int_list=[]
length=len(int_list)
print(length)
count,int_list=count_inversion(int_list,length)
print(count)
#print(type(int_list[0]))
#print(int_list)
#print(length)
#print('Hello')
