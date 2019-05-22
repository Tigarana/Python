import random


class targetWord:
    'This class holds the object that is the target word.'
    targetSuggestions = ['boek', 'vulkaan', 'luxe', 'winderig', 'romantisch',
                         'januel', 'onweer', 'kostelijk', 'vriendelijk', 'luchtballon',
                         'inleiding', 'verdoven', 'aardappelmesje', 'verdacht', 'muzikaal',
                         'ondergoed', 'volwassen', 'vogelnest', 'olifant', 'giraf',
                         'kriebelen', 'verbinding', 'nostalgisch', 'omschrijving', 'jaloers']

    def __init__(self, target=targetSuggestions[random.randint(0, len(targetSuggestions))]):
        self.target = target  # if you don't fill in a target, a random one will be picked
        self.displayLetter = [0]*len(target)

    def check(self, guess):
        succes = ''
        l = len(guess)
        if l == 1:
            succes = self.guessLetter(guess)
        elif l == len(self.target):
            succes = self.guessWord(guess)
        else:
            print('Please either type a single letter or a word of correct length.')
        return succes

    def guessLetter(self, letter):
        if letter in self.target:
            self.flagFound(letter)
            print('Good guess!')
            if sum(self.displayLetter) == len(self.displayLetter):  # All letters are found
                self.guessWord(self.target)
            return True
        else:
            print('Too bad...')
            return False

    def flagFound(self, letter):
        'Will be [] if letter is not in target'
        i = 0
        for ch in self.target:
            if ch == letter:
                self.displayLetter[i] = 1
            i += 1

    def guessWord(self, word):
        if word == self.target:
            print('Congratualations! You won ... well nothing. ')
            self.displayLetter = [1]*len(self.displayLetter)
            return True
        else:
            print('Too bad, maybe next time.')
            return False

    def displayWord(self):
        for i in range(0, len(self.target)):
            if self.displayLetter[i] == 1:
                print(self.target[i], end='', flush=True)
            else:
                print('.', end='', flush=True)

    def gameWon(self):
        return (len(self.displayLetter) == sum(self.displayLetter))
