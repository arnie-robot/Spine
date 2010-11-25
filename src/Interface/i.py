### Spine by Chris Alexander

# Standard imports
import socket

# Interface class
class I(object):

    # Default host and port
    host = "192.168.1.1"
    port = "25000"

    # The socket
    socket = None

    # Initialise with host and ports required
    def __init__(self, host = None, port = None):
        self.host = host or "192.168.1.1"
        self.port = port or 25000

    # Initialise function to start up the socket
    def initialise(self):
        if self.socket is None:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            print "Socket already initialised"

    # Shutdown closes the socket if it is active
    def shutdown(self):
        if self.socket:
            self.socket.shutdown()
