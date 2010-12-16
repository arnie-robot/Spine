### Spine by Chris Alexander

# Standard imports
import time
import threading
import Queue

# Custom imports
import Interface
import Thread

# Input Thread class
class Input(Thread.Interface):

    # How long to wait for a response from the socket
    waitTimeout = 500

    # Whether or not this thread is running
    running = 0

    # Whether there is a pending read on this request
    doRead = 0

    # Value from the last read
    value = None

    # The (redundant?) request queue
    requestQueue = None

    # Initialise the input thread
    def __init__(self, host, port, converter = None):
        # Initialise the parent
        self.requestQueue = Queue.Queue()
        super(Input, self).__init__(self.requestQueue)
        self.configureInterface(host, port, converter)

    # Init the interface
    def configureInterface(self, host, port, converter):
        if self.interface is None or self.interface.host != host or self.interface.port != port:
            # Initialise a new Interface
            self.interface = Interface.Input(host, port)
            self.interface.dataformat = converter
            self.interface.initialise()
            # Change our name
            self.setName(host + ":" + str(port))

    # Run loop for this thread
    def run(self):
        self.running = 1
        while self.running == 1:
            if self.doRead > 0:
                self.value = self.interface.receive()
                self.doRead = 0
            time.sleep(0.0001)
        self.interface.shutdown()

    # Stop this thread
    def stop(self):
        self.running = 0

    # Allows someone to read from this thread
    def read(self):
        self.doRead = 1
        i = 0
        while self.doRead > 0 and i < self.waitTimeout:
            time.sleep(0.0005)
            i += 1
        return self.value