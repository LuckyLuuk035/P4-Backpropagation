from __future__ import print_function


class Neuron:
    def __init__(self, weights, bias):
        self.w = weights
        self.b = bias
        self.e = 2.718281828459045
        self.a = None  # Error

    def __str__(self):
        return "output:"

    def activate(self, event):
        som = 0
        for i in range(len(self.w)):
            som = som + event[i] * self.w[i]
        output = som + self.b
        self.sigmoid_function(output)
        return output

    def sigmoid_function(self, result):
        # calculate the error
        self.a = 1 / (1 + self.e ** -result)  # Error
