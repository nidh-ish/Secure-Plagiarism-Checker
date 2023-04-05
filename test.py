from time import sleep
from queue import Queue
from threading import Thread
from multiprocessing import Process
import multiprocessing


def getmethod(q):
  i = 0
  while True:
    if not q.empty():
        print(q.get())
        i = i+1
    else:
      print("not getting")
    if i==100:
      break
    
    sleep(0.3)


def putmethod(q):
  for i in range(10):
    q.put(i)
    sleep(0.4)
    print("putted")


que = multiprocessing.Queue()

p1 = Process(target = getmethod, args = [que])
p2 = Process(target = putmethod, args = [que])


p1.start()
p2.start()

p1.join()
p2.join()