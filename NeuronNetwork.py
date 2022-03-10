from NeuronLayer import NeuronLayer


class NeuronNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.count = 0
        self.msg = ""

    def __str__(self):
        for output in self.layers[-1].neurons.values():
            self.msg += str(output) + "\n"
        return self.msg

    def feed_forward(self, event):
        # event[0]: input, event[1]: target
        # Activate layer
        self.layers[self.count].activate(event)
        self.count += 1
        if self.count < len(self.layers):
            # Go to next layer with values of layer before it.
            self.feed_forward([list(self.layers[self.count-1].neurons.values()), event[1]])
        else:
            self.count = 0
            print(self)
