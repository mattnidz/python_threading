
import threading
import time
import os
import platform

exitFlag = 0

class myThread(threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print_random_dir(self.name, self.counter, 5)
      #get_machine_type(self.name, self.counter, 5)
      print("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

def print_random_dir(threadName, delay, counter):
    while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print("%s: %s" % (threadName, os.listdir()))
      counter -= 1

# def get_machine_type(threadName, delay, counter):
#     while counter: 
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, platform.machine()) )
#         counter -= 1

# def get_platform_type(threadName, delay, counter):
#     while counter: 
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, platform.platform()) )
#         counter -= 1

# def get_system_type(threadName, delay, counter):
#     while counter: 
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print("%s: %s" % (threadName, platform.system() ) )
#         counter -= 1


# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(3, "Thread-3", 3)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()

# Wait for Threads to terminate
thread1.join() 
thread2.join()
thread3.join()
print("Exiting Main Thread")