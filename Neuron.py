from __future__ import print_function


class Neuron:
    def __init__(self, weights, bias):
        self.w = weights
        self.b = bias
        self.e = 2.718281828459045
        self.output = None
        self.error = None

    def __str__(self):
        return str(self.error)

    def activate(self, event):
        # event[0]: input, event[1]: target
        som = 0
        for i in range(len(self.w)):
            som = som + event[0][i] * self.w[i]
        self.output = som + self.b
        a = self.sigmoid_function(self.output)
        self.error = a * (1 - a) * -(event[1]-a)
        return self.output

    def calculate_error(self):  # for hidden neuron
        s = self.sigmoid_function()

    def sigmoid_function(self, result):
        return 1 / (1 + self.e ** -result)
