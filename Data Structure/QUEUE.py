from collections import deque
import threading
import time

class Queue:
    def __init__(self):
        self.buffer=deque()
    
    def enqueue(self,data):
        self.buffer.appendleft(data)
            
    def dequeue(self):
        return self.buffer.pop()
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]
    
    def isempty(self):
        return (len(self.buffer)==0)

    def produce_binary_numbers(self,data):
        numbers_queue = Queue()
        numbers_queue.enqueue("1")

        for i in range(data):
            front = numbers_queue.front()
            numbers_queue.enqueue(front + "0")
            numbers_queue.enqueue(front + "1")

            numbers_queue.dequeue()    

if __name__=='__main__':
    q=Queue()
   