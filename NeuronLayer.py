from Neuron import Neuron


class NeuronLayer:
    def __init__(self, neurons=None):
        self.neurons = neurons

    def __str__(self):
        msg = " | "
        for n in self.neurons:
            msg += str(n) + " | "
        msg += "|"
        return msg

    def activate(self, event):
        for n in self.neurons:
            n.activate(event)

    def addNeurons(self, amount):
        for i in range(amount):
            self.neurons += Neuron([0, 0], 0)

    def getOutput(self):
        return [i.output for i in self.neurons]
