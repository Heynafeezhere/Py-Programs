def TOH(n,source,destination,aux):
    if n==1:
        print("Move disk 1 From source",source,"to Destination",destination)
        return
    TOH(n-1,source,aux,destination)
    print("Move disk",n,"from source",source,"to Destination",destination)
    TOH(n-1,aux,destination,source)

if __name__ == "__main__":
    n=6
    TOH(n,'A',"B","C")