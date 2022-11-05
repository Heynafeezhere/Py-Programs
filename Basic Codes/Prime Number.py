num=int(input("Enter a number:"))
flag=0
if num>1:
    for i in range(2,num):
        if num%i==0:
            flag = 1
            break
if flag==1:
    print("The given num is not a prime num")
else:
    print("Prime num")        