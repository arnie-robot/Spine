#!/usr/bin/python

### Spine by Chris Alexander

# Standard imports


# Custom imports
import DataFormat
import Interface

# Begin execution
if __name__ == '__main__':
    o = Interface.Output("192.168.1.2", 25002)
    o.initialise()
    o.dataformat = DataFormat.SimulinkConverter()
    o.send(10)

    #i = Interface.Input("192.168.1.1", 25000)
    #i.initialise()
    #print i.receive()