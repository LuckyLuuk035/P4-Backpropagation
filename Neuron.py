from __future__ import print_function


class Neuron:
    def __init__(self, name, w=None):
        self.name = name
        self.b = 0
        self.e = 2.718281828459045
        self.error = 0
        self.msg = -1
        if w is None:
            w = []
        self.w = w

    def __str__(self):
        return self.msg

    def activate(self, event):
        self.msg = ""
        som = 0
        for i in range(len(self.w)):
            self.msg += "'" + str(event[i]) + "i " + str(self.w[i]) + "w" + "'  "
            som = som + event[i] * self.w[i]
        self.msg += str(self.b) + "b  "
        z = som + self.b
        self.msg += "o " + str(z)
        return z

    def sigmoid_function(self, z):
        return 1 / (1 + self.e ** -z)  # a

    def errorOutput(self, event, target):
        # inputthing = self.sigmoid_function(event) * (1 - self.sigmoid_function(event))
        outputthing = self.activate(event) * (1 - self.activate(event))
        print(outputthing)
        outputthing = outputthing * -(target - self.activate(event))
        self.error = outputthing
        print(outputthing)

    # def update(self, truthtable, epochs=25, show=False):
    #     for i in range(epochs):
    #         for row in truthtable:
    #             y = row[0]  # true value / target
    #             x = row[1]  # input
    #
    #             z = self.activate(x)  # output
    #             a = self.sigmoid_function(z)
    #             self.error = (z * (1 - z)) * -(y - z)
    #
    #
    #             # self.cost += c**2
    #             # CtoAl = 2 * (a - y)
    #             # self.msg += "    t:   " + str(y)
    #
    #             if show:
    #                 print(self)
    #             elif i + 1 == epochs:
    #                 print(self)
    #     # self.cost = self.cost / epochs
    #     # print(self.cost)
