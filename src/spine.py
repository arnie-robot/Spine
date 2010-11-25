#!/usr/bin/python

### Spine by Chris Alexander

# Standard imports


# Custom imports
import DataFormat
import Interface

# Begin execution
if __name__ == '__main__':
    #o = OutputInterface("192.168.1.2", 25000)
    #o.initialise()
    #o.send("Test")

    i = Interface.Input("192.168.1.1", 25000)
    i.initialise()
    print i.receive()