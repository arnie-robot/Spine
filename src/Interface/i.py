### Spine by Chris Alexander

# Standard imports
import socket

# Interface I class
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
        # Shut it down if it is started already
        if self.socket is not None:
            self.socket.shutdown()
        # Restart
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    

    # Shutdown closes the socket if it is active
    def shutdown(self):
        if self.socket:
            self.socket.shutdown()
