# Spine by Chris Alexander

# Standard imports

# Custom imports

# Thread Message class
class Message():

    # Host and port for this message / where it was from
    host = None
    port = None

    # Message contained in this object
    message = None

    # Initialise with default values
    def __init__(self, host, port, message):
        self.host = host
        self.port = port
        self.message = message