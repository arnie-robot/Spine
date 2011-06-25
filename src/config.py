### Spine by Chris Alexander

# Standard imports
import json
import logging

# Custom imports
import DataFormat
import Thread

# Class for loading and executing configurations
class Config(object):

    # The loaded configuration
    config = None;

    # The log levels
    loglevels = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warning': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}

    # Converter for aiding with data conversions
    converter = None

    # Constructor
    def __init__(self, conf = 'config.json'):
        # Load config
        self.config = json.load(open(conf, 'r'))

        # Load converter
        self.converter = DataFormat.Converter()

        # set up log level
        loglevel = self.loglevels.get(self.config['loglevel'], logging.NOTSET)
        logging.basicConfig(level=loglevel)
        logging.debug("Configuration: " + str(self.config))
        logging.info("Log level: " + self.config['loglevel'])

    # Return the InputPool completely configured
    def getInputPool(self):
        i = Thread.InputPool(self.getNameHostPort('input'))
        i.transforms['default'] = self.config['transforms']['default']
        for name, data in self.config['interfaces']['input'].items():
            if name in self.config['transforms'].keys():
                i.transforms[self.config['host'] + ':' + str(data['port'])] = self.config['transforms'][name]
            i.converters[self.config['host'] + ':' + str(data['port'])] = self.converter.getConverter(data['format'])
            i.connect(self.config['host'], data['port'], data['streamed'])
        return i

    # Return the OutputPool completely configured
    def getOutputPool(self):
        o = Thread.OutputPool(self.getNameHostPort('output'))
        o.transforms['default'] = self.config['transforms']['default']
        for name, data in self.config['interfaces']['output'].items():
            if name in self.config['transforms'].keys():
                o.transforms[data['host'] + ':' + str(data['port'])] = self.config['transforms'][name]
            o.converters[data['host'] + ':' + str(data['port'])] = self.converter.getConverter(data['format'])
        return o

    # Return an Output Interface's information
    def getOutputInfo(self, interface):
        if interface in self.config['interfaces']['output'].keys():
            return self.config['interfaces']['output'][interface]
        return None

    # Returns the connections that we are to maintain
    def getConnections(self):
        logging.debug("Connections: " + str(self.config['connections']))
        return self.config['connections']

    # Returns a list of host and port keyed by name of the connection
    def getNameHostPort(self, target):
        if target != "input" and target != "output":
            return None
        names = {}
        for name, data in self.config['interfaces'][target].items():
            if target == 'input':
                host = self.config['host']
            else:
                host = data['host']
            names[name] = (host, data['port'])
        return names