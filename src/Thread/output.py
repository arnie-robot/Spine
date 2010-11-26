### Spine by Chris Alexander

# Standard imports
import time
import threading

# Custom imports
import Interface
import Thread

# Output Thread class
class Output(threading.Thread):

    # Amount of time to sleep between not having any requests
    sleepTime = 0.1

    # The queue that is used for requests
    requestQueue = None

    # The interface we are using
    interface = None

    # Initialise the output thread
    def __init__(self, requestQueue):
        self.requestQueue = requestQueue
        super(Output, self).__init__()

    # Run loop for this thread
    def run(self):
        while True:
            # Fetch something from the queue
            item = self.requestQueue.get()
            if isinstance(item, Thread.Terminator):
                # Terminator received
                if self.interface is not None:
                    # If there is a valid interface still active, shut it down
                    self.interface.shutdown()
                break
            if isinstance(item, Thread.Message):
                # A valid message is found, so process it accordingly
                if self.interface is None or self.interface.host != item.host or self.interface.port != item.port:
                    if self.interface is not None:
                        # Shutdown existing interface if it exists
                        self.interface.shutdown()
                    self.interface = Interface.Output(item.host, item.port)
                    self.interface.initialise()
                self.interface.send(item.message)
                continue
            # Nothing valid found so come back soon
            time.sleep(self.sleepTime)