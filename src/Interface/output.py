### Spine by Chris Alexander

# Standard imports

# Custom imports
from dataformat import *
from interface import *

# OutputInterface class
class Output(Interface, DataFormat):

    # Initialise the OutputInterface
    def __init__(self, host = None, port = None):
        # Init the parent Interface
        super(Output, self).__init__(host, port)

    # Initialisation for the Output
    def initialise(self):
        # Initialise the parent interface
        super(Output, self).initialise()

    # Send data packet through the interface
    def send(self, data, ignoreFormat = 0):
        # Perform output conversion
        if self.dataformat and not ignoreFormat:
            data = self.dataformat.outputConvert(data);
        # Dispatch the data
        self.socket.sendto(data, (self.host, self.port))