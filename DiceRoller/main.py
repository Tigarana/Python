'Imports'
import setOfDice

'Declare variables'
DnDSet = [2, 4, 6, 8, 10, 12, 20, 100]
mySetOfDice = setOfDice.setOfDice()

'Declare functions'


def getOrdinalNumberSuffix(number):
    lastNumber = number % 10
    lastTenth = number % 100
    if (lastNumber in [1, 2, 3]) and (lastTenth not in [11, 12, 13]):
        if lastNumber == 1:
            return "st"
        elif lastNumber == 2:
            return "nd"
        elif lastNumber == 3:
            return "rd"
        else:
            print("Error in number suffix. ")
            return "th"
    else:
        return "th"


'Start program'
print("Welcome. You are here to create a set of DnD dice. ")

'Specify number of dice'
numDice = None
while numDice == None:
    numDiceStr = input("How many dice would you want in your set? ")
    try:
        numDice = int(numDiceStr)
        if numDice < 1:
            print("Specify a number larger than 0. ")
            numDice = None
    except ValueError:
        print("You can only type numbers. Please try again. \n")
    except:
        print("An unexpected error occured. The program will terminate.")
        quit()
print("You've created a set with %d dice. \n" % numDice)

'Give values to the dice'
print("Please specify how many sides every dice have.")
for i in range(0, numDice):
    ordinal = getOrdinalNumberSuffix(i+1)
    numEyes = None
    while numEyes == None:
        numEyesStr = input(
            "How many sides does the %d%s dice have? " % (i+1, ordinal))
        try:
            numEyes = int(numEyesStr)
            if numEyes not in DnDSet:
                print("Please only use the number of eyes from following set: ")
                print(*DnDSet, sep=", ", end='\n')
                numEyes = None
            else:
                mySetOfDice.createDice(numEyes)
        except ValueError:
            print("You can only type numbers. Please try again. \n")
        except:
            print("An unexpected error occured. The program will terminate.")
            quit()
    print("You've created a %d-sided dice.\n" % numEyes)
print("All your dice are created. \n")

'Roll dice?'
print("Do you want to roll the dice? ")
rollBool = None
while rollBool == None:
    rollBool = input("Please type 'y' for yes and 'n' for no. ")
    if rollBool not in ['y', 'n']:
        print("Please ONLY type 'y' or 'n'!")
        rollBool = None
    elif rollBool == 'y':
        print("\nDice are rolled.")
        mySetOfDice.rollSetOfDice()
    elif rollBool == 'n':
        print("\nSo sorry to hear you don't want to roll any dice. Maybe next time? ")
