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
        for n in self.neurons:
            self.neurons[n] = n.activate(event)