from unittest import TestCase

from Neuron import Neuron
from NeuronLayer import NeuronLayer
from NeuronNetwork import NeuronNetwork
import random


class TestNeuronNetwork(TestCase):
    def test_train_and(self):
        # bij deze testcasus gaan we de AND-gate testen.
        # maak neuron aan met random start waarde
        o = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)],
                   random.uniform(-1, 1))
        output_later = NeuronLayer([o])
        and_gate = NeuronNetwork([output_later])

        and_gate.train([[0, 0], [1, 0], [0, 1], [1, 1]], [0, 0, 0, 1], ["epochs", 1000], 0.2, False)
        for i in [[[0, 0], 0], [[0, 1], 0], [[1, 0], 0], [[1, 1], 1]]:
            # i[0] = input, i[1] = expected output
            self.assertEqual(and_gate.feed_forward(i[0])[0], i[1], "And-gate should return " + str(i[1]))

    def test_train_xor(self):
        # Maak neurons aan met random start waarde
        f = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
        g = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
        o = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
        # Maak layers
        hidden_layer = NeuronLayer([f, g])
        output_layer = NeuronLayer([o])
        xorGate = NeuronNetwork([hidden_layer, output_layer])
        # Train netwerk
        xorGate.train([[0, 0], [1, 0], [0, 1], [1, 1]], [0, 1, 1, 0], ["time", 5], 0.3, False)

        # Test netwerk
        for i in [[[0, 0], 0], [[0, 1], 0], [[1, 0], 0], [[1, 1], 1]]:
            # i[0] = input, i[1] = expected output
            xorGate.feed_forward(i[0])
            print(xorGate.feed_forward(i[0]))
            self.assertEqual(xorGate.feed_forward(i[0]), i[1], "Xor-gate should return " + str(i[1]))

    def test_train_halfadder(self):
        h = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
        i = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

        hiddenLayer = NeuronLayer([h, i])

        j = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))
        k = Neuron([random.uniform(-1, 1), random.uniform(-1, 1)], random.uniform(-1, 1))

        outputLater = NeuronLayer([j, k])

        halfAdder = NeuronNetwork([hiddenLayer, outputLater])

        halfAdder.train([[0, 0], [1, 0], [0, 1], [1, 1]], [[0, 0], [1, 0], [1, 0], [0, 1]], ["epochs", 1000], 0.3, False)

        # Test netwerk
        for i in [[[0, 0], 0], [[0, 1], 0], [[1, 0], 0], [[1, 1], 1]]:
            # i[0] = input, i[1] = expected output
            halfAdder.feed_forward(i[0])
            self.assertEqual(halfAdder.feed_forward(i[0]), i[1], "Xor-gate should return " + str(i[1]))
