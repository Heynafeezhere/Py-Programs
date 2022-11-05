#implementation
class Hashtable:
    def __init__(self):
        self.max=100
        self.arr=(None for i in range(self.max))
    
    def get_hash(key):
        h=0
        for char in key:
            h+=ord(char) #returns the aski value of char
        print(h%100) 

    def __setitem__(self,key): #adding value
        b=self.get_hash(key)
        print(self.arr[b])
            
    def __getitem__(self,key): #Searching
        c=self.get_hash(key)
        print( self.arr[c])

    
    def __delitem__(self,key): #Deleting
        d=self.get_hash(key)
        self.arr[d]=None
    
if __name__== '__main__':
    t = Hashtable()
    t.get_hash()
    
   
