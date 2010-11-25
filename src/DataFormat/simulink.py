### Spine by Chris Alexander

# Standard imports
import struct

# Simulink class
class Simulink(object):

    # Packs data into a format suitable for Simulink
    def pack(self, data):
        return struct.pack("d", data)

    # Unpacks data sent by Simulink
    def unpack(self, data):
        return struct.unpack("d", data)[0]

    # Converts a string to its binary representation
    def tobin(self, data):
        return ''.join([''.join(['10'[not (m&ord(x))] for m in
        (128,64,32,16,8,4,2,1)]) for x in data])

    # Converts a string to its hexadecimal representation
    def tohex(self, data):
        return ''.join(hex(ord(x)) for x in data)
