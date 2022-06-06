import unittest

from Neuron import Neuron
from NeuronLayer import NeuronLayer
from NeuronNetwork import NeuronNetwork
import test_NeuronNetwork
import random

print("xorGate")


h = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
i = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

hiddenLayer = NeuronLayer([h, i])

j = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
k = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

outputLater = NeuronLayer([j, k])

halfAdder = NeuronNetwork([hiddenLayer, outputLater])

halfAdder.train([[0, 0], [1, 0], [0, 1], [1, 1]], [[0, 0], [1, 0], [1, 0], [0, 1]], ["epochs", 1000])

#Run above or below

if __name__ == '__main__':
    testsuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=1).run(testsuite)
