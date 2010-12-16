#!/usr/bin/python

### Spine by Chris Alexander

# Standard imports
import Queue
import time
import copy

# Custom imports
import DataFormat
import Interface
import Thread

# Main execution function
def main():

    i = Thread.InputPool()
    i.converters['192.168.1.1:25000'] = DataFormat.CSVConverter()
    i.connect("192.168.1.1", 25000, True)

    o = Thread.OutputPool()
    o.converters['192.168.1.80:25001'] = DataFormat.SimulinkConverter()

    val = None
    sentVal = None
    j = 0
    while (1 == 1):
        val = i.read("192.168.1.1", 25000)
        if not j % 100:
            if sentVal != val:
                sendval = copy.copy(val)
                sendval[0] = (320-int(sendval[0]))/2
                sendval[1] = (480-int(sendval[1]))/2
                sendval[2] = (700-int(sendval[2]))/3
                print val
                print sendval
                o.send(Thread.Message("192.168.1.80", 25001, sendval))
                sentVal = val
                print "Sent"
        j += 1

# Boilerplate
if __name__ == '__main__':
    main()