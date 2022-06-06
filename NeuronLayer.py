class NeuronLayer:
    def __init__(self, neurons):
        self.neurons = neurons

    def __str__(self):
        msg = " | "
        for n in self.neurons:
            msg += str(n) + " | "
        msg += "|"
        return msg

    def activate(self, event):
        for n in self.neurons:
            n.activate(event)

    def getOutput(self):
        return [i.output for i in self.neurons]
