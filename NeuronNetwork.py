import time


class NeuronNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.count = 0
        self.total_loss = 0
        self.start_values = None  # output van input neurons
        self.lr = 0.2  # learningrate

    def __str__(self):
        msg = ""
        for i, l in enumerate(self.layers):
            msg += str(i) + " " + str(l) + "\n"
        return msg

    def train(self, inputs, targets, stopconditie, learning_rate=None, print_=True):
        epochs = 0
        start_time = time.time()
        if learning_rate:
            self.lr = learning_rate
        while self.check_stop(stopconditie, epochs, start_time):
            for count, inp in enumerate(inputs):
                self.feed_forward(inp)
                self.calculate_errors(targets[count])
                deltas = self.calculate_deltas()
                self.update(deltas)
                self.start_values = None
            epochs += 1
            if print_:
                if stopconditie[0] == "time":
                    print("epoch: " + str(epochs) + " | total loss: " + str(round(self.total_loss, 3)) + "\n" +
                          " | time left: " + str(round(stopconditie[1] - (time.time() - start_time), 3)) + "\n" + str(
                        self))
                else:
                    print("epoch: " + str(epochs) + " | total loss: " + str(round(self.total_loss, 3)) + "\n" + str(self))

    def check_stop(self, stopconditie, epochs, start_time):
        if stopconditie[0] == "epochs" and stopconditie[1] > epochs:
            return True  # Continue
        elif stopconditie[0] == "loss" and stopconditie[1] < self.total_loss:
            return True  # Continue
        elif stopconditie[0] == "time" and stopconditie[1] > (time.time() - start_time):
            return True  # Continue
        else:
            return False  # Stop

    def feed_forward(self, event):
        # event[0]: input, event[1]: target
        if not self.start_values:
            self.start_values = event
        output = self.layers[self.count].activate(event)

        self.count += 1
        if self.count < len(self.layers):
            # Go to next layer with values of layer before it.
            self.feed_forward(self.layers[self.count - 1].getOutput())
        else:
            self.count = 0
            for c, i in enumerate(output):
                if i > 0:
                    output[c] = 1
                else:
                    output[c] = 0
            return output

    def calculate_errors(self, target):
        self.layers.reverse()
        for i, l in enumerate(self.layers):
            for count, n in enumerate(l.neurons):
                n.calculate_error(i, self, target, count)
        self.layers.reverse()

    def calculate_deltas(self):
        delta_lst = []
        self.layers.reverse()
        for i, l in enumerate(self.layers):
            layer_deltas = []
            for n in l.neurons:
                weight_deltas = []
                for count, w in enumerate(n.w):  # voor alle weights
                    if i == len(self.layers) - 1:
                        a = self.start_values[count]
                    else:
                        a = self.layers[i + 1].neurons[count].a
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
            for count, n in enumerate(l.neurons):  # layer
                for k, d in enumerate(deltas[i][count][0]):  # neuron
                    n.w[k] = n.w[k] - d
                n.bias = n.bias - deltas[i][count][1]
        self.layers.reverse()
