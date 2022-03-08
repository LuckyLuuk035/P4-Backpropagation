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

    # def sigmoid_function(self, z):
    #     return 1 / (1 + self.e ** -z)  # a
    #
    # def errorOutput(self, event, target):
    #     # inputthing = self.sigmoid_function(event) * (1 - self.sigmoid_function(event))
    #     outputthing = self.activate(event) * (1 - self.activate(event))
    #     print(outputthing)
    #     outputthing = outputthing * -(target - self.activate(event))
    #     self.error = outputthing
    #     print(outputthing)

#     def activate(self, event):
#         self.msg = ""
#         som = 0
#         for i in range(len(self.w)):
#             self.msg += "'" + str(event[i]) + "i " + str(self.w[i]) + "w" + "'  "
#             som = som + event[i] * self.w[i]
#         self.msg += str(self.b) + "b  "
#         z = som + self.b
#         self.msg += "o " + str(z)
#         return z
