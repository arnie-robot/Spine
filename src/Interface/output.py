### Spine by Chris Alexander

# Standard imports
import numpy

# Custom imports
import DataFormat
import Interface

# Interface Output class
class Output(Interface.I, DataFormat.Format):

    # Initialise the OutputInterface
    def __init__(self, host = None, port = None):
        # Init the parent Interface
        super(Output, self).__init__(host, port)

    # Initialisation for the Output
    def initialise(self):
        # Initialise the parent interface
        super(Output, self).initialise()

    # Send data packet through the interface
    def send(self, data, ignoreFormat = 0, ignoreTransform = 0):
        # Transform data
        if self.transform and not ignoreTransform:
            # Apply the transform
            transform = numpy.matrix(str(self.transform))
            data.append('1')
            datamatrix = numpy.matrix(';'.join(map(str, data)))
            resultmatrix = transform.I*datamatrix
            data2 = resultmatrix.tolist()
            data = []
            for i in data2:
                data.append(i[0])
            data = data[:-1]
        # Perform output conversion
        if self.dataformat and not ignoreFormat:
            data = self.dataformat.outputConvert(data);
        # Dispatch the data
        self.socket.sendto(data, (self.host, self.port))