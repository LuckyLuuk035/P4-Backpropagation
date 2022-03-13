from NeuronLayer import NeuronLayer


class NeuronNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.count = 0
        self.error = None
        self.startvalues = None # output van input neurons
        self.lr = 1  # learningrate
        self.msg = ""

    def __str__(self):
        self.msg = ""
        for output in self.layers[-1].neurons.values():
            self.msg += str(output) + "\n"
        return self.msg

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
            self.count = 0

    def calculate_errors(self, target):
        self.layers.reverse()
        for i, l in enumerate(self.layers):
            for n in l.neurons:
                n.calculate_error(i,  target)
        self.layers.reverse()

    def calculate_deltas(self):
        delta_lst = []
        self.layers.reverse()
        o = list(self.layers[0].neurons.keys())[0]  # output neuron ((Maak hier nog van dat het voor elk element in de list werkt))
        for i in range(len(o.w)):  # voor alle weights
            if len(self.layers) != 1:
                output_i = list(self.layers[1].neurons.keys())[i].output
            else:
                output_i = self.startvalues[i]
            gradient = output_i * o.error
            delta_lst.append(self.lr * gradient)
        delta_lst = [delta_lst, self.lr * o.error]
        # print(delta_lst)
        return delta_lst

    def update(self, deltas):
        # deltas[0]: delta's for the weights, deltas[1]: delta for bias
        o = list(self.layers[0].neurons.keys())[0]  # output neuron
        for i, d in enumerate(deltas[0]):
            o.w[i] = o.w[i] - d
        o.b = o.b - deltas[1]
        print(o.w, o.b)
        self.layers.reverse()
