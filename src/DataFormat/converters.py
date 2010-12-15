# Spine by Chris Alexander

# Standard imports
import array

# Custom imports
import DataFormat

# Converter for Simulink connections
class SimulinkConverter(DataFormat.Converter):
    
    s = None

    def __init__(self):
        self.s = DataFormat.Simulink()

    def input(self, data):
        return self.s.unpack(data)

    def output(self, data):
        if (type(data) == type(float())) or (type(data) == type(int())):
            data = self.s.pack(data)
        else:
            raise DataFormat.Exception("Cannot perform output conversion on invalid data type", type(data))
        return data

class CSVConverter(DataFormat.Converter):

    s = None

    def __init__(self):
        self.s = DataFormat.CSV()

    def input(self, data):
        return self.s.explode(data)

    def output(self, data):
        return self.s.implode(data)