# Spine by Chris Alexander

# Standard imports
import array

# Custom imports
import DataFormat

# Converter for Simulink connections
class SimulinkConverter(DataFormat.Converter):

    # The simulink converter
    s = None

    # The size of the input units
    inputUnit = 8

    def __init__(self):
        self.s = DataFormat.Simulink()

    def input(self, data):
        arr = []
        for i in range(len(data)/self.inputUnit):
            arr.append(self.s.unpack(data[(i*self.inputUnit):((i+1)*self.inputUnit)]))
        return arr

    def output(self, data):
        if (type(data) == type(float())) or (type(data) == type(int())):
            data = self.s.pack(data)
        elif (type(data) == type(list()) or type(data) == type(tuple())):
            if type(data) == type(tuple()):
                data = list(data)
            for i, item in enumerate(data):
                data[i] = self.s.pack(int(item))
            data = ''.join(data)
        else:
            raise DataFormat.Exception("Cannot perform output conversion on invalid data type", type(data))
        return data

class CSVConverter(DataFormat.Converter):

    s = None

    def __init__(self):
        self.s = DataFormat.CSV()

    def input(self, data):
        if isinstance(data, basestring):
            return self.s.explode(data)

    def output(self, data):
        if (type(data) == type(list())) or (type(data) == type(tuple())):
            return self.s.implode(data)