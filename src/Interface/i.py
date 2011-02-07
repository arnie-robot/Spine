### Spine by Chris Alexander

# Standard imports
import socket
import numpy

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
            self.socket.close()

    def applyTransform(self, data, invert = False):
        # Apply the transform to each element
        retdata = []
        for d in data:
            if (len(d) < 3):
                retdata.append([float(i) for i in d])
                continue
            elif (len(d) == 3):
                d_coord = d
                d_extras = []
            else:
                d_coord = d[0:3]
                d_extras = d[3:]
            transform = numpy.matrix(str(self.transform))
            d_coord.append('1')
            datamatrix = numpy.matrix(';'.join([str(i) for i in d_coord]))
            if invert:
                resultmatrix = transform.I*datamatrix
            else:
                resultmatrix = transform*datamatrix
            data2 = resultmatrix.tolist()
            coord = []
            for i in data2:
                coord.append(i[0])
            coord = coord[:-1]
            coord.extend([float(i) for i in d_extras])
            retdata.append(coord)
        return retdata
