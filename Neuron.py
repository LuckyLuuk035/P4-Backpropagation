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
        som = 0
        for i in range(len(self.w)):
            som = som + event[i] * self.w[i]
        self.output = som + self.b
        # self.calculate_error(a, event[1], output_l)
        return self.output

    def calculate_error(self, layer,  target):
        # output_l: {False = hidden, True = Output}
        a = self.sigmoid_function(self.output)
        if layer == 0:
            self.error = a * (1 - a) * -(target - a)
        else:
            self.error = a * (1 - a) * -(target - a)


    def sigmoid_function(self, result):
        return 1 / (1 + self.e ** -result)
