from threading import Thread,Lock
import os
import time


database_value = 0

def increase(lock):
    global database_value

    lock.acquire()
    #processing
    local_copy = database_value
    local_copy+= 1
    time.sleep(0.1)
    database_value = local_copy
    lock.release()

if __name__ == "__main__":
    print("start value",database_value)

    lock = Lock()
    #(lock,) The comma indicates that the value is a tuple
    thread1 = Thread(target=increase,args=(lock,))
    thread2 = Thread(target=increase,args=(lock,))
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("endmain")
    print("end value",database_value)
