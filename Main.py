from Neuron import Neuron
from NeuronLayer import NeuronLayer
from NeuronNetwork import NeuronNetwork
import random


n1 = Neuron("AND-gate")
n1.b = random.uniform(-1, 1)
n1.w = [random.uniform(-1, 1), random.uniform(-1, 1)]

p2 = Neuron("OR-gate")
p2.b = random.uniform(-1, 1)
p2.w = [random.uniform(-1, 1), random.uniform(-1, 1)]

# print("AND-gate")
# n1.update([[0, [0, 0]], [0, [0, 1]], [0, [1, 0]],  [1, [1, 1]]], 30)
# print("OR-gate")
# p2.update([[0, [0, 0]], [1, [0, 1]], [1, [1, 0]], [1, [1, 1]]], 30)

nl1 = NeuronLayer("first layer")


n3 = Neuron("AND-gate")
n3.b = 0.5
n3.w = [0.3, 0.3]

n3.errorOutput([0, 1], 1)
print(n3)
