# Spine by Chris Alexander

# Standard imports

# Custom imports
import DataFormat

# Converter for Simulink connections
class SimulinkConverter(DataFormat.Converter):

    def inputConvert(self, data):
        return data

    def outputConvert(self, data):
        s = DataFormat.Simulink()
        if (type(data) == type(tuple())):
            data = ''.join(s.pack(i) for i in data)
        elif (type(data) == type(float())) or (type(data) == type(int())):
            data = s.pack(data)
        else:
            raise DataFormat.Exception("Cannot perform output conversion on invalid data type", type(data))
        return data