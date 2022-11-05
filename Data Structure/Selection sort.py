def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(min_index+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i],arr[min_index] = arr[min_index],arr[i]

if __name__=="__main__":
    arr = [31,13,23,43,12,43254,643,674,52]
    selection_sort(arr)
    print(arr)