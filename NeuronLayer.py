class NeuronLayer:
    def __init__(self, neurons):
        self.neurons = {}
        for n in neurons:
            self.neurons[n] = None  # Value: output

    def __str__(self):
        msg = "| | "
        for n in self.neurons:
            msg += str(n) + " | "
        msg += "|"
        return msg

    def activate(self, event):
        for n in self.neurons:
            self.neurons[n] = n.activate(event)
