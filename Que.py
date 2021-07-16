from threading import Thread,Lock
from queue import Queue 
import time

def worker(q,lock):
    while True:
        value= q.get()


if __name__ == "__main__":

    q=Queue()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker)
        thread.deamon = True
        thread.start()

    q.put(1)
    q.put(2)
    q.put(3)

    first = q.get()
    print(first)
    #after processing with q.get() we should write 
    #q.task_done to ensure that our task is completed
    q.task_done()
    q.join()

    print("endmain")