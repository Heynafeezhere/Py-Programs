import numpy as np
n=int(input())
arr=[]
arr1=[]
arr2=[]
for i in range(0,n):
    arr.append(int(input()))
print(arr)
q=int(input())
c=int(input())
if q>c:
    max=q
else:
    max=c
for i in range(0,max):
    a,b=map(int,input().split())
    arr1.append(a)
    arr2.append(b)
max1=len(arr1)

max2=len(arr2)
if max1>max2:
    final_max=max1
else:
    final_max=max2 
for x in range(0,q):
    for y in range(0,q+1):
        if(x==y):
            i=arr1[x]
            j=arr2[y]
            print("row",i)
            print("column",j)
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            print(arr)
        
for i in range(0,n):
    print("Ans",arr[i])
    
