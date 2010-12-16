# Spine by Chris Alexander

# Standard imports

# Custom imports
import Thread

# Output Pool class
class InputPool(Thread.Pool):

    # Connect to a port
    def connect(self, host, port, streamed = False):
        exist = self.findThread(host, port)
        if exist is None:
            converter = None
            if host + ":" + str(port) in self.converters:
                converter = self.converters[host + ":" + str(port)]
            if streamed:
                thread = Thread.StreamedInput(host, port, converter)
            else:
                thread = Thread.Input(host, port, converter)
            thread.start()
            self.threads.append(thread)

    # Disconnect from a port
    def disconnect(self, host, port):
        exist = self.findThread(host, port)
        if exist is None:
            return None
        self.threads[exist].shutdown()

    # Reads a value from the host/port
    def read(self, host, port):
        thread = self.findThread(host,port)
        if thread is None:
            return False
        return self.threads[thread].read()