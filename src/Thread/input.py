### Spine by Chris Alexander

# Standard imports
import time
import threading

# Custom imports
import Interface
import Thread

# Input Thread class
class Input(Thread.Interface):

    # How long to wait for a response from the socket
    waitTimeout = 1000

    # Whether or not this thread is running
    running = 0

    # Whether there is a pending read on this request
    read = 0

    # Value from the last read
    value = None

    # Initialise the output thread
    def __init__(self, requestQueue):
        # Init the interface
        if self.interface is None or self.interface.host != item.host or self.interface.port != item.port:
            # Initialise a new Interface
            self.interface = Interface.Input(item.host, item.port)
            self.interface.initialise()
            # Change our name
            self.setName(item.host + ":" + str(item.port))
        # Initialise the parent
        super(Input, self).__init__(requestQueue)

    # Run loop for this thread
    def run(self):
        self.running = 1
        while self.running == 1:
            if self.read > 0:
                self.value = self.interface.receive()
                self.read = 0
            time.sleep(0.0005)
        self.interface.shutdown()

    # Stop this thread
    def stop(self):
        self.running = 0

    # Allows someone to read from this thread
    def read(self):
        self.read = 1
        i = 0
        while self.read > 0 and i < self.waitTimeout:
            time.sleep(0.0005)
            i += 1
        return self.value