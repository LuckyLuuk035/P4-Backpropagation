class NeuronLayer:
    def __init__(self, neurons, outputlayer=False):
        self.neurons = {}
        for n in neurons:
            self.neurons[n] = None  # Value: output
        self.outputlayer = outputlayer
        self.msg = ""

    def __str__(self):
        for n in self.neurons:
            self.msg += n + " output: " + self.neurons.get(n)
        return self.msg

    def activate(self, event):
        # event[0]: input, event[1]: target
        for n in self.neurons:
            self.neurons[n] = n.activate(event, self.outputlayer)
            # loss: sigmoid_function on the result

    def get_error(self, index=None):
        lst = []
        if index:
            return self.neurons[index].error
        else:
            for n in self.neurons:
                lst.append(n.error)
        return lst
