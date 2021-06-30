from multiprocessing import Process
import os
import time 

processes =[]

def square_numbers():
    for i in range(100):
        print(i*i)


num_processes = os.cpu_count()
print(num_processes)

#create processes

for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

#start
for p in processes:
    p.start()

#join 
for p in processes:
    p.join()

print("end main")

