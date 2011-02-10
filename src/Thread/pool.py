# Spine by Chris Alexander

# Standard imports
import time
import threading

# Custom imports

# Output Pool class
class Pool(threading.Thread):

    # Maximum number of permitted threads
    maxThreads = 5

    # Specifies how long to wait between thread checks
    findTimeout = 0.005

    # The threads themselves
    threads = []

    # Converters for the threads
    converters = {}

    # Transforms for the threads
    transforms = {}

    # Lookup table for the thread names to host/port combos
    names = {}

    # Initialisation the pool and start the threads
    def __init__(self, names, autostart = True):
        super(Pool, self).__init__()

        # Yet to figure out why we need to blank these off on init
        # Let's just say it screws up otherwise :)
        self.threads = []
        self.converters = {}
        self.transforms = {}

        # Load in the name lookups
        self.names = names

        if autostart:
            self.start()

    # Run for the thread - nothing to do here
    def run(self):
        pass

    # Finds an already running thread for the host and port
    def findThread(self, host, port, iter = 0):
        for i, thread in enumerate(self.threads):
            if thread.getName() == host + ":" + str(port):
                return i
        if iter > 0:
            # Break out if this is more than the first time
            return None
        # It takes time to register a thread - so just check once more
        time.sleep(self.findTimeout)
        return self.findThread(host, port, iter + 1)

    # Returns a thread based on its name
    def findThreadByName(self, name):
        for k, v in self.names.items():
            if (k == name):
                return self.findThread(v[0], v[1])
        return None

    # Returns the thread object itself
    def getThread(self, host, port):
        return self.threads[self.findThread(host, port)]