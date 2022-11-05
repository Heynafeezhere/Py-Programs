def ForwardShift(text,n):
    text = text.upper()
    char = ''
    for i in range(0,len(text)):
        a = ord(text[i])
        b = a + n
        if b > 90:
           b = b - 26
        char += chr(b)
        i = i +1
    return char

    
def BackwardShift(text,n):
    text = text.upper()
    text = text[::-1]
    char = ''
    for i in range(0,len(text)):
        a = ord(text[i])
        b = a + n
        if b > 90:
           b = b - 26
        char += chr(b)
        i = i +1
    return char
    

   





if __name__ == "__main__":
    text= str(input())
    n = int(input())
    print(BackwardShift(text,n))


