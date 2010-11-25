### Spine by Chris Alexander

# Standard imports

# InterfaceFormat class
class Format(object):

    # Holds the name for the format
    dataformat = None

    # Function to convert input data into something useful
    def inputConvert(self, data):
        return data

    # Function to convert data to be output from Python to the output format
    def outputConvert(self, data):
        return data
