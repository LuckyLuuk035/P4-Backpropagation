from Neuron import Neuron
from NeuronLayer import NeuronLayer
from NeuronNetwork import NeuronNetwork
import random

# onderstaande gegevens zijn op basis van de uitwerkingen van les 6.

print("andGate")
o = Neuron([-0.5, 0.5], 1.5)  # [-0.5, 0.5], 1.5 OR [1, 1], -1.5

outputLater = NeuronLayer([o])

andGate = NeuronNetwork([outputLater])

andGate.train([[0, 0], [1, 0], [0, 1], [1, 1]], [0, 0, 0, 1])
# for i in [[[0, 0], 0], [[1, 0], 0], [[0, 1], 0], [[1, 1], 1]]:
#     andGate.feed_forward(i)

print("xorGate")

f = Neuron([0.2, -0.4], 0)
g = Neuron([0.7, 0.1], 0)
hiddenLayer = NeuronLayer([f, g])

o = Neuron([0.6, 0.9], 0)
outputLater = NeuronLayer([o])

xorGate = NeuronNetwork([hiddenLayer, outputLater])

for i in [[[0, 0], 0], [[1, 0], 1], [[0, 1], 1], [[1, 1], 0]]:
    xorGate.feed_forward(i)
