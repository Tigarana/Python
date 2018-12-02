'Test the dice class'
import dice
import setOfDice

'Make a dice'
d1 = dice.dice(6)  # Creates a 6 sided dice
d1.rollDice()

diceSet1 = setOfDice.setOfDice()
diceSet1.addDice(d1)
'Print diceset'
diceSet1.getNumberOfDice()
diceSet1.getSetOfDice()

diceSet1.createMultipleDice(4, 10)
'Print diceset'
diceSet1.getNumberOfDice()
diceSet1.getSetOfDice()

'Roll set of dice'
diceSet1.rollSetOfDice()
