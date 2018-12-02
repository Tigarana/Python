import random


class dice:
    'Common base class for all dice'

    # numSides = 0
    # numEyes = 0

    def __init__(self, numSides):
        self.numSides = numSides

    def rollDice(self):
        self.numEyes = random.randint(1, self.numSides)

    def getResult(self):
        print("The number of eyes rolled is %d" % self.numEyes)
        return self.numEyes

    def getNumSides(self):
        print("The number of sides is %d" % self.numSides)
        return self.numSides
