from Neuron import Neuron
from NeuronLayer import NeuronLayer
from NeuronNetwork import NeuronNetwork
import random


# onderstaande gegevens zijn op basis van de uitwerkingen van les 6.
m = Neuron([1, 0], 0)
n = Neuron([0, 1], 0)

o = Neuron([-0.5, 0.5], 1.5)

inputLayer = NeuronLayer([m, n])
outputLater = NeuronLayer([o])

andGate = NeuronNetwork([inputLayer, outputLater])

andGate.feed_forward([0, 0])


