import time
import threading

def calc_square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("Square:",n*n)
def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("Cube:",n*n*n)
    
if __name__=="__main__":
    t=time.time()
    arr=[2,3,4,5,6]
    t1=threading.Thread(target=calc_square, args=(arr,))
    t2=threading.Thread(target=calc_cube, args=(arr,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done in:",time.time()-t)