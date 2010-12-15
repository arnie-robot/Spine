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

    i = Thread.InputPool()
    i.connect("192.168.1.1", 25000)

    o = Thread.OutputPool()

    val = None
    sentVal = None
    j = 0
    while (1 == 1):
        val = i.read("192.168.1.1", 25000)
        if not j % 1000:
            print val
            if sentVal != val:
                o.send(Thread.Message("192.168.1.1", 25001, val))
                sentVal = val
                print "\tSent"
        j += 1

# Boilerplate
if __name__ == '__main__':
    main()