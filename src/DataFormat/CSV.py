### Spine by Chris Alexander

# Standard imports

# Custom imports

# DataFormat Simulink class
class CSV(object):

    # Explodes a CSV string into a tuple
    def explode(self, data):
        return data.split(',')

    # Implodes a set of data into a CSV string
    def implode(self, data):
        return data.join(',')