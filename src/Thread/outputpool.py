# Spine by Chris Alexander

# Standard imports
import time
import threading
import random
import Queue

# Custom imports
import Thread

# Output Pool class
class OutputPool(Thread.Pool):

    # The queue used for sending in requests to the pool
    queue = None

    # Queues for the threads
    threadQueues = []

    # Initialisation for the pool
    def __init__(self, names):
        self.queue = Queue.Queue()
        super(OutputPool, self).__init__(names)

    # Run the pool
    def run(self):
        while True:
            # Clean up any dead / removed threads
            self.clean()
            item = self.queue.get()
            if isinstance(item, Thread.Message):
                self.assignToThread(item)
                # We want to carry on if there are items still in the queue
                continue
            if isinstance(item, Thread.Terminator):
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
        threadid = self.findThreadByName(item.name)
        data = self.names[item.name]
        item.host = data[0]
        item.port = data[1]
        if threadid is not None:
            # Found a thread to give it to, so dispatch to there
            self.threadQueues[threadid].put(item)
        else:
            if len(self.threads) >= self.maxThreads:
                # Too many threads already - so stick it in a random one
                self.threadQueues[random.randint(0, len(self.threads)-1)].put(item)
            else:
                # Got space - start a new thread for it
                self.startThread(item)

    # Start a new thread and pass the given message into it
    def startThread(self, message):
        threadqueue = Queue.Queue()
        threadqueue.put(message)
        thread = Thread.Output(threadqueue)
        if message.host + ":" + str(message.port) in self.converters:
            thread.converter = self.converters[message.host + ":" + str(message.port)]
        thread.transform = self.transforms["default"]
        if message.host + ":" + str(message.port) in self.transforms:
            thread.transform = self.transforms[message.host + ":" + str(message.port)]
        thread.start()
        self.threads.append(thread)
        self.threadQueues.append(threadqueue)

    # Stops a specific thread
    def stopThread(self, thread):
        if thread < 0 or thread > len(self.threads):
            return
        self.threadQueues[thread].put(Thread.Terminator())

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
    def clean(self):
        i = 0
        for thread in self.threads:
            if not thread.isAlive():
                self.threads.pop(i)
                # Clean up its queue by passing them back into the pool
                self.queue.extend(self.threadQueues[i])
                self.threadQueues.pop(i)
            i += 1