from NeuronLayer import NeuronLayer


class NeuronNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.total_loss = 0  # this is not correct yet
        self.count = 0
        self.error = None
        self.lr = 1  # learningrate
        self.msg = ""

    def __str__(self):
        self.msg = ""
        for output in self.layers[-1].neurons.values():
            self.msg += str(output) + "\n"
        return self.msg

    def feed_forward(self, event):
        # event[0]: input, event[1]: target
        self.layers[self.count].activate(event)
        self.count += 1
        if self.count < len(self.layers):
            # Go to next layer with values of layer before it.
            self.feed_forward([list(self.layers[self.count-1].neurons.values()), event[1]])
        else:
            error = self.layers[-1].get_error(0)[-1]  # haal hier de index weg van je voor de adder gaat.
            print(error)
            self.calculate_deltas()  # <<<currently working on this>>>
            self.count = 0

    def calculate_gradient(self, n1, n2):
        return n1.output * n2.error

    def calculate_deltas(self):
        print("yo", self.layers[-1].neurons.values)
        # self.calculate_gradient(n1, n2)
