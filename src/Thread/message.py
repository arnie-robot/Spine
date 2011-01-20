# Spine by Chris Alexander

# Standard imports

# Custom imports

# Thread Message class
class Message():

    # Name, host, port for the connection where this message is from/to
    name = None
    host = None
    port = None

    # Message contained in this object
    message = None

    # Initialise with default values
    def __init__(self, name, message):
        self.name = name
        self.message = message