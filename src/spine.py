#!/usr/bin/python

### Spine by Chris Alexander

# Standard imports
import time
import copy
import signal
import sys
import logging
import math

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
    sentData = {}
    while (True):
        # Store up the previous data we had
        previousData = copy.copy(inputData)

        # Load up input data from all of the connections
        inputData = {}
        for connection in connections:
            if connection['input'] not in inputData.keys():
                inputData[connection['input']] = i.read(connection['input'])

        # Decide if we want to dispatch any data
        for connection in connections:

            # Check that past and previous data exists
            if (connection['input'] in previousData.keys()) and \
                (connection['input'] in inputData.keys()):

                # Decide if our past and previous data is different
                if (previousData[connection['input']] != inputData[connection['input']]):

                    # We have decided we do want to dispatch
                    t = time.gmtime()
                    timestring = str(t[3]) + ":" + str(t[4]) + ":" + str(t[5])

                    # See if we need to do a threshold check, and if it is possible
                    outputInfo = c.getOutputInfo(connection['output']) # load up data
                    if "threshold" in outputInfo.keys() and connection['output'] in sentData.keys():
                        # We need to do the check
                        checkElementsCount = 3
                        if "checkElementsCount" in outputInfo:
                            checkElementsCount = outputInfo['checkElementsCount']

                        # Do the calculation
                        squared = 0
                        for k in range(checkElementsCount):
                            inputval = inputData[connection['input']][0][k]
                            sentval = sentData[connection['output']][0][k]
                            squared = squared + math.fabs(math.pow(inputval - sentval, 2))
                        diff = math.sqrt(squared)

                        if diff > outputInfo['threshold']:
                            # We are over the limit, we need to die
                            logging.debug(timestring + ": Aborted dispatch: " + connection['input'] + " => " + connection['output'] + ", " + str(diff) + " is greater than " + str(outputInfo['threshold']))
                            break;

                    # No check or check passed
                    logging.debug(timestring + ": Dispatching: " + connection['input'] + " => " + connection['output'] + " - " + str(inputData[connection['input']]))
                    sentData[connection['output']] = copy.copy(inputData[connection['input']]) # Log we sent this
                    o.send(Thread.Message(connection['output'], copy.copy(inputData[connection['input']]))) # copy value or it goes BAD

# Signal handler
def signal_handler(signal, frame):
    sys.exit(0)

# Boilerplate
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()