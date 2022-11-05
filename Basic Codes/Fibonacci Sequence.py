#Fibonacci Sequence
num=int(input("Enter the limit of the fibonacci sequence:"))
n1=0
n2=1
count=0
if num<1:
    print("Enter a positive integer!")
elif num==0:
    print(n1)
else:
    print("Fibonacci Sequence:")
    n=0 
    while count<num:
        print(n)
        n=n1+n2
        n1=n2
        n2=n
        count+=1