### Spine by Chris Alexander

# Standard imports
import time
import threading
import Queue

# Custom imports
import Interface
import Thread

# Input Thread class
class StreamedInput(Thread.Input):

    # Init the interface
    def configureInterface(self, host, port, converter):
        if self.interface is None or self.interface.host != host or self.interface.port != port:
            # Initialise a new Interface
            self.interface = Interface.StreamedInput(host, port)
            self.interface.dataformat = converter
            self.interface.initialise()
            # Change our name
            self.setName(host + ":" + str(port))

    # Run loop for this thread
    def run(self):
        self.interface.start()

    # Stop this thread
    def stop(self):
        self.interface.stop()

    # Allows someone to read from this thread
    def read(self):
        return self.interface.lastValue