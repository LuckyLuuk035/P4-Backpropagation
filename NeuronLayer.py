from Neuron import Neuron


class NeuronLayer:
    def __init__(self, neurons):
        if type(neurons) == int:
            self.neurons = []
            self.addNeurons(neurons)
        elif type(neurons) == list:
            self.neurons = neurons

    def __str__(self):
        msg = " | "
        for n in self.neurons:
            msg += str(n) + " | "
        msg += "|"
        return msg

    def activate(self, event):
        return_lst = []
        for n in self.neurons:
            return_lst.append(n.activate(event))
        return return_lst

    def addNeurons(self, amount):
        for i in range(amount):
            self.neurons.append(Neuron([0, 0], 0))

    def getOutput(self):
        return [i.output for i in self.neurons]
