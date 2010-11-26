# Spine by Chris Alexander

# Standard imports
import time
import threading
import random
import Queue

# Custom imports
import Thread

# Output Pool class
class OutputPool(threading.Thread):

    # Maximum number of permitted threads
    maxThreads = 5

    # The queue used for sending in requests to the pool
    queue = None

    # The threads themselves
    threads = []

    # Queues for the threads
    threadQueues = []

    # Initialisation for the pool
    def __init__(self):
        self.queue = Queue.Queue()
        super(OutputPool, self).__init__()

    # Run the pool
    def run(self):
        while True:
            # Clean up any dead / removed threads
            self.cleanPool()
            item = self.queue.get()
            if isinstance(item, Thread.Message):
                self.assignToThread(item)
                # We want to carry on if there are items still in the queue
                continue
            if isinstance(item, Thread.Terminator):
                print "Deactivated"
                break
        # Now shut down the threads
        self.stopAll()
        while self.checkAlive() > 0:
            time.sleep(0.0001)

    # Sends an item through the output system
    def send(self, message):
        self.queue.put(message)

    # Stops the thread pool
    def stop(self):
        self.queue.put(Thread.Terminator())

    # Assigns a message item to a thread, accounting for existing values etc.
    def assignToThread(self, item):
        threadid = self.findThread(item.host, item.port)
        if threadid is not None:
            # Found a thread to give it to, so dispatch to there
            self.threadQueues[threadid].put(item)
            print "Item added to thread " + str(threadid)
        else:
            if len(self.threads) >= self.maxThreads:
                # Too many threads already - so stick it in a random one
                self.threadQueues[random.randint(0, len(self.threads)-1)].put(item)
                print "Item added to random thread"
            else:
                # Got space - start a new thread for it
                self.startThread(item)
                print "New thread started"

    # Finds an already running thread for the host and port
    def findThread(self, host, port, iter = 0):
        i = 0;
        for thread in self.threads:
            if thread.getName() == host + ":" + str(port):
                return i
            i += 1
        if iter > 0:
            # Break out if this is more than the first time
            return None
        # It takes time to register a thread - so just check once more
        time.sleep(0.005)
        return self.findThread(host, port, iter + 1)

    # Start a new thread and pass the given message into it
    def startThread(self, message):
        threadqueue = Queue.Queue()
        threadqueue.put(message)
        thread = Thread.Output(threadqueue)
        thread.start()
        self.threads.append(thread)
        self.threadQueues.append(threadqueue)

    # Stop all the threads in this pool
    def stopAll(self):
        for i in self.threadQueues:
            i.put(Thread.Terminator())

    # Checks the number of currently active threads in the pool
    def checkAlive(self):
        count = 0
        for thread in self.threads:
            if thread.isAlive():
                count += 1
        return count

    # Cleans the thread pool if threads are dead etc.
    def cleanPool(self):
        i = 0
        for thread in self.threads:
            if not thread.isAlive():
                self.threads.pop(i)
                # Clean up its queue by passing them back into the pool
                self.queue.extend(self.threadQueues[i])
                self.threadQueues.pop(i)
            i += 1