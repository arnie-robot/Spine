# Spine

Spine is an open-source, python-powered signal marshalling system for anthropomorphic robot systems.

The aim of the project is to provide a spine-like (in the human sense) component in an anthropomorphic robot to enable communication
between processing units and input and output sources in a managed way.

It includes a number of packages outlined below

## Packages

The base package includes spine.py which is the initialiser for configuring the Spine instance to be run, with its given configuration.

### DataFormat

This package provides translation facilities between a number of data formats and the internal Python formats.

This allows efficient conversion of data into and out of the application when communicating with other nodes.

### Interface

This package provides interfacing capabilities for dispatching, receiving individual and receiving streamed data over the network.

### Thread

Provides thread pooling, input and output pools, thread signalling messengers in order to coordinate a set of threads to do whatever you want