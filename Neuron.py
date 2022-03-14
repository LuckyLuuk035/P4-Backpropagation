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
        return str(self.error)

    def activate(self, event):
        som = 0
        for i in range(len(self.w)):
            som = som + event[i] * self.w[i]
        self.output = som + self.b
        return self.output

    def calculate_error(self, i, layer, target, weight):
        # output_l: {False = hidden, True = Output}
        if i == 0:
            self.a = self.sigmoid_function(self.output)
            self.error = self.a * (1 - self.a) * -(target - self.a)
        else:
            self.a = self.sigmoid_function(sum(self.w))
            print(self.a)
            for n in layer.neurons:
                self.error = 0
                self.error += self.a * (1 - self.a) * n.w[weight] * n.error

    def sigmoid_function(self, result):
        return 1 / (1 + self.e ** -result)
