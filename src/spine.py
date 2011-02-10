#!/usr/bin/python

### Spine by Chris Alexander

# Standard imports
import time
import copy
import signal
import sys
import logging

# Custom imports
import Thread
from config import *

# Main execution function
def main():
    
    # No logging before this point as we will not have loaded the configuration yet
    c = Config()
    logging.info("Configuration loaded")

    logging.info("Loading configued inputs and outputs")
    i = c.getInputPool()
    o = c.getOutputPool()
    logging.info("Inputs and outputs loaded")
    connections = c.getConnections()
    logging.info("Connections loaded")

    logging.info("Initialising connections")
    inputData = {}
    while (True):
        previousData = copy.copy(inputData)
        inputData = {}
        for connection in connections:
            if connection['input'] not in inputData.keys():
                inputData[connection['input']] = i.read(connection['input'])
        for connection in connections:
            if (connection['input'] in previousData.keys()) and \
                (connection['input'] in inputData.keys()):
                if (previousData[connection['input']] != inputData[connection['input']]):
                    
                    t = time.gmtime()
                    timestring = str(t[3]) + ":" + str(t[4]) + ":" + str(t[5])
                    logging.debug(timestring + ": Dispatching: " + connection['input'] + " => " + connection['output'])
                    o.send(Thread.Message(connection['output'], copy.copy(inputData[connection['input']]))) # copy value or it goes BAD

# Signal handler
def signal_handler(signal, frame):
    sys.exit(0)

# Boilerplate
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()