### Spine by Chris Alexander

# Standard imports

# Custom imports

# DataFormat Simulink class
class CSV(object):

    # Explodes a CSV string into a tuple
    def explode(self, data):
        items = data.split(';')
        arr = []
        for i in items:
            arr.append(i.split(','))
        return arr

    # Implodes a set of data into a CSV string
    def implode(self, data, char = ','):
        return char.join([str(i) for i in data])