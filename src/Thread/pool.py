# Spine by Chris Alexander

# Standard imports
import time
import threading

# Custom imports
import Thread

# Output Pool class
class Pool(threading.Thread):

    # Maximum number of permitted threads
    maxThreads = 5

    # Specifies how long to wait between thread checks
    findTimeout = 0.005

    # The threads themselves
    threads = []

    # Run for the thread - nothing to do here
    def run(self):
        pass

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
        time.sleep(self.findTimeout)
        return self.findThread(host, port, iter + 1)