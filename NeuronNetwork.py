from NeuronLayer import NeuronLayer

class NeuronNetwork:
    def __init__(self, NetworkName):
        self.name = NetworkName
        self.layers = []
        self.output = []
        self.count = 0
        self.msg = ""

    def __str__(self):
        return self.msg

    def addPerceptronLayer(self, perceptron):
        # voeg de perceptron layers toe aan het netwerk
        if type(perceptron) == NeuronLayer:
            self.layers.append(perceptron)

        elif type(perceptron) == list:
            for p in perceptron:
                self.addPerceptronLayer(p)

    def feed_forward(self, event):
        self.msg = ""
        layer = self.layers[self.count]
        result = layer.activate(event)
        self.msg += str(layer)
        self.count += 1
        if self.count < len(self.layers):
            self.feed_forward(result)
        else:
            self.count = 0
            return result
