from NeuronLayer import NeuronLayer


class NeuronNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.count = 0
        self.msg = ""

    def __str__(self):
        for output in self.layers[-1].neurons.values():
            self.msg += str(output) + "\n"
        return self.msg

    def feed_forward(self, event):
        # event[0]: input, event[1]: target
        # Activate layer
        self.layers[self.count].activate(event)
        self.count += 1
        if self.count < len(self.layers):
            # Go to next layer with values of layer before it.
            self.feed_forward([list(self.layers[self.count-1].neurons.values()), event[1]])
        else:
            self.count = 0
            print(self)

    # def feed_forward(self, event=None):
    #     if event:
    #         # This only happens on the first layer. (activates layer with input)
    #         self.layers[self.count].activate(event)
    #
    #     else:
    #         # Activate layer with the output from the layer before it.
    #         self.layers[self.count].activate(list(self.layers[self.count-1].neurons.values()))
    #     self.count += 1
    #     if self.count < len(self.layers):
    #         self.feed_forward()
    #     else:
    #         self.count = 0
    #         print(self)

#     def feed_forward(self, event):
#
#         if self.count == 0:
#             # only on inputlayer
#             inputlayer = self.layers[self.count]
#             for i in range(len(inputlayer)):
#                 # geef de juiste input aan de juiste input neuron
#                 inputlayer.neurons[i].activate(i)
#
#         self.msg = ""
#         layer = self.layers[self.count]
#         result = layer.activate(event)
#         self.msg += str(layer)
#         self.count += 1
#         if self.count < len(self.layers):
#             self.feed_forward(result)
#         else:
#             self.count = 0
#             return result
