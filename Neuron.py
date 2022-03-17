from __future__ import print_function


class Neuron:
    def __init__(self, weights, bias):
        self.w = weights
        self.b = bias
        self.e = 2.718281828459045
        self.a = None
        self.output = None
        self.error = None

    def __str__(self):
        msg = "{ w["
        for i in self.w:
            if i > 0:
                msg += " "
            msg += str(round(i, 3)) + " "
        msg += "] b"
        if self.b > 0:
            msg += " "
        msg += str(round(self.b, 3)) + " }"
        return msg

    def activate(self, event):
        som = 0
        for i in range(len(self.w)):
            som = som + event[i] * self.w[i]
        self.output = som + self.b
        return self.output

    def calculate_error(self, i, network, target, weight):
        if i == 0:
            self.error = 0
            self.a = self.sigmoid_function(self.output)
            if type(target) == list:
                for j in range(len(network.layers[0].neurons)):
                    self.error += self.a * (1 - self.a) * -(target[j] - self.a)
            else:
                self.error += self.a * (1 - self.a) * -(target - self.a)
        else:
            self.error = 0
            self.a = self.sigmoid_function(sum(self.w))
            for n in network.layers[i-1].neurons:
                self.error += self.a * (1 - self.a) * n.w[weight] * n.error

    def sigmoid_function(self, result):
        return 1 / (1 + self.e ** -result)
