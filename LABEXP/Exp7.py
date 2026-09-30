from threading import Thread, Lock
from queue import Queue
from multiprocessing import Process

q = Queue()
lock = Lock()

def producer():
    for i in range(1, 6):
        q.put(i)
        print("Produced:", i)
    q.put(None)

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        with lock:
            print("Consumed:", item)

def run():
    t1 = Thread(target=producer)
    t2 = Thread(target=consumer)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    run()
