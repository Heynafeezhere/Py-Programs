from collections import deque

class stack:
    def __init__(self):
        self.box=deque()
    def push(self,data):
        self.box.append(data)
    def pop(self):
        return self.box.pop()
        
    def peek(self):
        print(self.box[-1])
    def isempty(self):
        print(len(self.box)==0)
    def size(self):
        return len(self.box)
    
    def rev(self,s):
        Stack = stack()

        for ch in s:
            Stack.push(ch)
        rtr=''
        while Stack.size()!=0:
            rtr += Stack.pop()
        return rtr
            

if __name__=='__main__':
    s=stack()
    print(s.rev("I am the king"))