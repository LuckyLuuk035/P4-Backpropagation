import unittest

from Neuron import Neuron
from NeuronLayer import NeuronLayer
from NeuronNetwork import NeuronNetwork
from test_NeuronNetwork import TestNeuronNetwork
import random

print("AndGate")
o = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)],
           random.uniform(-1, 1))  # [-0.5, 0.5], 1.5 OR [1, 1], -1.5
output_later = NeuronLayer([o])
and_gate = NeuronNetwork([output_later])

and_gate.train([[0, 0], [1, 0], [0, 1], [1, 1]], [0, 0, 0, 1], ["time", 5])

print("xorGate")

f = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
g = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

hiddenLayer = NeuronLayer([f, g])

o = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
outputLater = NeuronLayer([o])

xorGate = NeuronNetwork([hiddenLayer, outputLater])

xorGate.train([[0, 0], [1, 0], [0, 1], [1, 1]], [0, 1, 1, 0], ["time", 5])

h = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
i = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

hiddenLayer = NeuronLayer([h, i])

j = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
k = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

outputLater = NeuronLayer([j, k])

halfAdder = NeuronNetwork([hiddenLayer, outputLater])

halfAdder.train([[0, 0], [1, 0], [0, 1], [1, 1]], [[0, 0], [1, 0], [1, 0], [0, 1]], ["epochs", 1000])

TestNeuronNetwork()

# if __name__ == '__main__':
#     # unittest.main()
#
#     testsuite = unittest.TestLoader().discover('.')
#     unittest.TextTestRunner(verbosity=1).run(testsuite)
