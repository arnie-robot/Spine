### Spine by Chris Alexander

# Standard imports

# Custom imports
import DataFormat

# DataFormat Converter class
class Converter(object):

    # Holds the name for the format
    dataformat = None

    # Function to convert input data into something useful
    def inputConvert(self, data):
        """arr = []
        for i in range(len(data)/self.inputUnit):
            arr.append(self.input(data[(i*self.inputUnit):((i+1)*self.inputUnit)]))
        return arr"""
        return self.input(data)

    # Function to convert data to be output from Python to the output format
    def outputConvert(self, data):
        if (type(data) == type(tuple())):
            data = ''.join(self.output(i) for i in data)
        else:
            data = self.output(data)
        return data

    # Convert a single input value
    def input(self, data):
        return data

    # Convert a single output value
    def output(self, data):
        return data

    # returns a converter based on those available
    def getConverter(self, converter):
        if converter == "simulink":
            return DataFormat.SimulinkConverter()
        elif converter == "csv":
            return DataFormat.CSVConverter()
        else:
            return None