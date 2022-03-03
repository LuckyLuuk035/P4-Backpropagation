from Neuron import Neuron

class NeuronLayer:
    def __init__(self, layerName):
        self.name = layerName
        self.neurons = []
        self.weights = 0
        self.msg = ""

    def __str__(self):
        return self.msg

    def addPerceptron(self, neuron):
        if type(neuron) == Neuron:
            if self.weights == 0:
                self.weights = len(neuron.weights)
                self.neurons.append(neuron)
            elif len(neuron.weights) == self.weights:
                self.neurons.append(neuron)
            else:
                raise EnvironmentError("aantal weights van:", neuron.name, "is niet correct")
        elif type(neuron) == list:
            for p in neuron:
                self.addPerceptron(p)

    def activate(self, event):
        output = []
        self.msg = ""
        for p in self.neurons:
            result = p.activate(event)
            self.msg += str(p)
            output.append(result)

        return output
