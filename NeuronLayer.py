class NeuronLayer:
    def __init__(self, neurons):
        self.neurons = {}
        for n in neurons:
            self.neurons[n] = None  # Value: output
        self.msg = ""

    def __str__(self):
        for n in self.neurons:
            self.msg += n + " output: " + self.neurons.get(n)
        return self.msg

    def activate(self, event):
        # event[0]: input, event[1]: target
        for n in self.neurons:
            self.neurons[n] = n.activate(event)
            # loss: sigmoid_function on the result

    def get_loss(self, index=None):
        lst = []
        if index:
            return self.neurons[index].a
        else:
            for n in self.neurons:
                lst.append(n.a)
        return lst
