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

    def activate(self, event, output_l=False):
        # event[0]: input, event[1]: target,  output_l: {False = hidden, True = Output}
        som = 0
        for i in range(len(self.w)):
            som = som + event[0][i] * self.w[i]
        self.output = som + self.b
        a = self.sigmoid_function(self.output)
        self.calculate_error(a, event[1], output_l)
        return self.output

    def calculate_error(self, a, target, output_l):
        # output_l: {False = hidden, True = Output}
        if output_l == True:
            self.error = a * (1 - a) * -(target - a)
        elif output_l == False:
            self.error = a * (1 - a) * -(target - a)
        else:
            print("ERROR!")



    def sigmoid_function(self, result):
        return 1 / (1 + self.e ** -result)
