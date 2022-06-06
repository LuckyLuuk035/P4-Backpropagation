from Neuron import Neuron
from NeuronLayer import NeuronLayer
from NeuronNetwork import NeuronNetwork
import random

# onderstaande gegevens zijn op basis van de uitwerkingen van les 6.

print("andGate")
o = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))  # [-0.5, 0.5], 1.5 OR [1, 1], -1.5

outputLater = NeuronLayer([o])

andGate = NeuronNetwork([outputLater])

# andGate.train([[0, 0], [1, 0], [0, 1], [1, 1]], [0, 0, 0, 1], ["time", 5])

print("xorGate")

f = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
g = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

hiddenLayer = NeuronLayer([f, g])

o = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
outputLater = NeuronLayer([o])

xorGate = NeuronNetwork([hiddenLayer, outputLater])

# xorGate.train([[0, 0], [1, 0], [0, 1], [1, 1]], [0, 1, 1, 0], ["time", 5])

h = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
i = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

hiddenLayer = NeuronLayer([h, i])

j = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
k = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

outputLater = NeuronLayer([j, k])

halfAdder = NeuronNetwork([hiddenLayer, outputLater])

halfAdder.train([[0, 0], [1, 0], [0, 1], [1, 1]], [[0, 0], [1, 0], [1, 0], [0, 1]], ["epochs", 1000])

print(halfAdder.feed_forward([[1, 1], [1, 1]]))
