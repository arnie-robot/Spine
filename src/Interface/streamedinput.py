### Spine by Chris Alexander

# Standard imports

# Custom imports
import DataFormat
import Interface

# Interface StreamedInput class
class StreamedInput(Interface.Input):

    # Holds the most recent data value received
    lastValue = None

    # Whether or not this connection should be active
    active = 0

    # Initialise the Interface
    def __init__(self, host = None, port = None):
        # Init the parent Interface
        super(StreamedInput, self).__init__(host, port)

    # Initialisation for the Input
    def initialise(self):
        # Initialise the parent interface
        super(StreamedInput, self).initialise()
        # Init this class
        self.lastValue = None
        self.active = 0

    # Starts this connection
    def start(self, ignoreFormat = 0):
        self.active = 1
        self.receive(ignoreFormat)

    # Stops this connection
    def stop(self):
        self.active = 0

    # Receive packets from the socket
    def receive(self, ignoreFormat = 0):
        while (self.active):
            self.lastValue = super(StreamedInput, self).receive(ignoreFormat)