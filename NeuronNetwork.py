from NeuronLayer import NeuronLayer


class NeuronNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.total_loss = 0
        self.count = 0
        self.msg = ""

    def __str__(self):
        self.msg = ""
        for output in self.layers[-1].neurons.values():
            self.msg += str(output) + "\n"
        return self.msg

    def feed_forward(self, event):
        # event[0]: input, event[1]: target
        # Activate layer
        self.layers[self.count].activate(event[0])
        self.count += 1
        if self.count < len(self.layers):
            # Go to next layer with values of layer before it.
            self.feed_forward([list(self.layers[self.count-1].neurons.values()), event[1]])
        else:
            # Get the total loss of output layer
            loss_lst = self.layers[-1].get_loss()
            for loss in loss_lst:
                self.total_loss += (event[1] - loss) ** 2
            print(self.total_loss)
            self.count = 0
