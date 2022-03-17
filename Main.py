from Neuron import Neuron
from NeuronLayer import NeuronLayer
from NeuronNetwork import NeuronNetwork
import random

# onderstaande gegevens zijn op basis van de uitwerkingen van les 6.

print("andGate")
o = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))  # [-0.5, 0.5], 1.5 OR [1, 1], -1.5

outputLater = NeuronLayer([o])

andGate = NeuronNetwork([outputLater])

# andGate.train([[0, 0], [1, 0], [0, 1], [1, 1]], [0, 0, 0, 1], ["time", 60])

print("xorGate")

f = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
g = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

# f = Neuron([0.2, -0.4], 0)
# g = Neuron([0.7, 0.1], 0)

hiddenLayer = NeuronLayer([f, g])

o = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
outputLater = NeuronLayer([o])

xorGate = NeuronNetwork([hiddenLayer, outputLater])

# xorGate.train([[0, 0], [1, 0], [0, 1], [1, 1]], [0, 1, 1, 0], 100)
