import time
from threading import current_thread, Thread
import random
from queue import Queue

# need to evaluate if the queue is full
queue = Queue(5)

class ProducerThread(Thread):
  def run(self):
    name = current_thread().getName()
    nums = range(100)
    global queue
    while True:
      num = random.choice(nums)
      queue.put(num)
      print('producer %s produced %s' %(name, num))
      t = random.randint(1, 3)
      time.sleep(t)
      print('producer %s slept %s seconds' %(name, t))
class ConsumerThread(Thread):
    def run(self):
      name = current_thread().getName()
      global queue
      while True:
        num = queue.get()
        queue.task_done()
        print('consumer %s consumed %s' %(name, num))
        t = random.randint(1, 5)
        time.sleep(t)
        print('consumer %s slept %s seconds' %(name, t))

p1 = ProducerThread(name='p')
p1.start()

c1 = ConsumerThread(name='c1')
c1.start()
c2 = ConsumerThread(name='c2')
c2.start()