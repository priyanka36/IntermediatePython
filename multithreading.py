from threading import Thread 
import os
import time 

def square_numbers():
    for i in range(10):
        print(i*i)
        time.sleep(0.1)

def cube_numbers():
    for i in range(10):
        print(i*i*i)
        time.sleep(0.1)

threads=[]

num_threads = 5

for i in range(num_threads):
    t=Thread(target=square_numbers)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("end main")