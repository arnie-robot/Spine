### Spine by Chris Alexander

# Standard imports
import time
import threading

# Custom imports
import Interface
import Thread

# Output Thread class
class Interface(threading.Thread):

    # Amount of time to sleep between not having any requests
    sleepTime = 0.1

    # The queue that is used for requests
    requestQueue = None

    # The interface we are using
    interface = None

    # Converter to use for the interface once it is instanciated
    converter = None

    # Initialise the interface thread
    def __init__(self, requestQueue):
        self.requestQueue = requestQueue
        super(Interface, self).__init__()

    # Run loop for this thread
    def run(self):
        pass