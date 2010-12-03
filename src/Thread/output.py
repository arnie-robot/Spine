### Spine by Chris Alexander

# Standard imports
import time
import threading

# Custom imports
import Interface
import Thread

# Output Thread class
class Output(Thread.Interface):

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
                    # Register we are changing name
                    self.setName("_" + item.host + ":" + str(item.port))
                    if self.interface is not None:
                        # Shutdown existing interface if it exists
                        self.interface.shutdown()
                    # Initialise a new Interface
                    self.interface = Interface.Output(item.host, item.port)
                    self.interface.initialise()
                    # Change our name
                    self.setName(item.host + ":" + str(item.port))
                self.interface.send(item.message)
                continue
            # Nothing valid found so come back soon
            time.sleep(self.sleepTime)