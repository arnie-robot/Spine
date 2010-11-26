#!/usr/bin/python

### Spine by Chris Alexander

# Standard imports
import Queue
import time

# Custom imports
import DataFormat
import Interface
import Thread

# Main execution function
def main():
    #o = Interface.Output("192.168.1.2", 25001)
    #o.initialise()
    #o.dataformat = DataFormat.SimulinkConverter()
    #o.send((10, 20, 30))
    
    #i = Interface.Input("192.168.1.1", 25000)
    #i.initialise()
    #i.dataformat = DataFormat.SimulinkConverter()
    #print i.receive()

    #s = Interface.StreamedInput("192.168.1.1", 25000)
    #s.initialise()
    #s.dataformat = DataFormat.SimulinkConverter()
    #s.start()

    q = Queue.Queue()
    i = Thread.Output(q)
    i.start()
    q.put(Thread.Message("192.168.1.2", 25000, "Hello, World"))
    time.sleep(1)
    q.put(Thread.Message("192.168.1.2", 25000, "Hello, World 2"))
    time.sleep(1)
    q.put(Thread.Message("192.168.1.2", 25000, "Hello, World 3"))
    q.put(Thread.Terminator())

# Boilerplate
if __name__ == '__main__':
    main()