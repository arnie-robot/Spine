### Spine by Chris Alexander

# Standard imports
import numpy

# Custom imports
import DataFormat
import Interface

# Interface Input class
class Input(Interface.I, DataFormat.Format):

    # The max number of bytes to receive from the socket
    maxBytesReceive = 2048

    # Initialise the Input Interface
    def __init__(self, host = None, port = None):
        # Init the parent Interface
        super(Input, self).__init__(host, port)

    # Initialisation for the Input
    def initialise(self):
        # Initialise the parent interface
        super(Input, self).initialise()
        # Bind the socket
        self.socket.bind((self.host, self.port))

    # Receive a single packet from the socket
    def receive(self, ignoreFormat = 0, ignoreTransform = 0):
        data, addr = self.socket.recvfrom(self.maxBytesReceive)
        if self.dataformat and not ignoreFormat:
            data = self.dataformat.inputConvert(data)
        if self.transform and not ignoreTransform:
            # Apply the transform
            transform = numpy.matrix(str(self.transform))
            data.append('1')
            datamatrix = numpy.matrix(';'.join(data))
            resultmatrix = transform*datamatrix
            data2 = resultmatrix.tolist()
            data = []
            for i in data2:
                data.append(i[0])
            data = data[:-1]
        return data