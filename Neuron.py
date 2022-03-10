from __future__ import print_function


class Neuron:
    def __init__(self, weights, bias):
        self.w = weights
        self.b = bias
        self.e = 2.718281828459045
        self.output = None
        self.msg = -1

    def __str__(self):
        return "output:", self.output

    def activate(self, event):
        som = 0
        for i in range(len(self.w)):
            som = som + event[i] * self.w[i]
        self.output = som + self.b
        return self.output

    def sigmoid_function(self):
        return 1 / (1 + self.e ** -self.output)  # a
