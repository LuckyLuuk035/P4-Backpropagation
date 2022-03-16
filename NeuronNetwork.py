from NeuronLayer import NeuronLayer


class NeuronNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.count = 0
        self.error = None
        self.startvalues = None  # output van input neurons
        self.lr = 1  # learningrate
        self.msg = ""

    def __str__(self):
        self.msg = ""
        for output in self.layers[-1].neurons.values():
            self.msg += str(output) + "\n"
        return self.msg

    def train(self, inputs, targets, epochs=100):
        for i in epochs:


    def feed_forward(self, event):
        # event[0]: input, event[1]: target
        if not self.startvalues:
            self.startvalues = event[0]
        self.layers[self.count].activate(event[0])
        self.count += 1
        if self.count < len(self.layers):
            # Go to next layer with values of layer before it.
            self.feed_forward([list(self.layers[self.count-1].neurons.values()), event[1]])
        else:
            self.calculate_errors(event[1])
            deltas = self.calculate_deltas()
            self.update(deltas)
            self.startvalues = None
            self.count = 0

    def calculate_errors(self, target):
        self.layers.reverse()
        for i, l in enumerate(self.layers):
            for j, n in enumerate(l.neurons):
                n.calculate_error(i, self.layers[i-1], target, j)
        self.layers.reverse()

    def calculate_deltas(self):
        delta_lst = []

        self.layers.reverse()
        for i, l in enumerate(self.layers):
            layer_deltas = []
            weight_deltas = []
            for n in list(l.neurons.keys()):
                weight_deltas = []
                for j, w in enumerate(n.w):  # voor alle weights
                    if i == len(self.layers)-1:
                        a = self.startvalues[j]
                    else:
                        a = list(self.layers[i+1].neurons.keys())[j].a
                    gradient = a * n.error
                    weight_deltas.append(self.lr * gradient)
                bias_delta = self.lr * n.error
                layer_deltas.append([weight_deltas, bias_delta])
            delta_lst.append(layer_deltas)
        self.layers.reverse()
        return delta_lst

    def update(self, deltas):
        self.layers.reverse()
        for i, l in enumerate(self.layers):  # network
            for j, n in enumerate(list(l.neurons.keys())):  # layer
                for k, d in enumerate(deltas[i][j][0]):  # neuron
                    n.w[k] = n.w[k] - d
                n.b = n.b - deltas[i][j][1]
        self.layers.reverse()
