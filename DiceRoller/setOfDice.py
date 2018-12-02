import dice


class setOfDice:
    'This class holds a set of dice. This set can have different dice with a different number of eyes'

    # numDice = 0
    # listDice = None

    def __init__(self):
        self.numDice = 0
        self.listDice = list()

    def createDice(self, numEyes):
        d = dice.dice(numEyes)
        self.numDice += 1
        self.listDice.append(d)

    def createMultipleDice(self, numNewDice, numEyes):
        for _ in range(0, numNewDice):
            self.createDice(numEyes)

    def addDice(self, dice):
        self.numDice += 1
        self.listDice.append(dice)

    def getNumberOfDice(self):
        print("The number of dice in the set is %d" % self.numDice)
        return self.numDice

    def getSetOfDice(self):
        print("Following dice are in the set: ")
        for d in self.listDice:
            print(d.numSides)
        return self.listDice

    def rollSetOfDice(self):
        totalNumberOfEyes = 0
        for d in self.listDice:
            d.rollDice()
            totalNumberOfEyes += d.getResult()
        print("Total number of rolled eyes is %d" % totalNumberOfEyes)
        return totalNumberOfEyes



