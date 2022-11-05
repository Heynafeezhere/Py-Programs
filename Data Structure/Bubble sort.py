def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        flag = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                flag = True
        if flag == False:
            break

if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    
    bubble_sort(elements)
    print(elements)
    elements = [1,2,3,4,2]

    bubble_sort(elements)
    print(elements)
    
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements)
    print(elements)