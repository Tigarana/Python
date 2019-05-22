
class hangmanDrawer:
    'This object will draw the hangman figure, depending on the amout of failed tries.'

    def __init__(self, maxTries = 10):
        self.failedTries = 0
        self.maxTries = maxTries

    def failedAttemt(self):
        self.failedTries += 1

    def drawHangman(self):
        for _ in range(0, self.failedTries):
            print(' X ', end='', flush=True)
        for _ in range(self.failedTries, self.maxTries):
            print(' O ', end='', flush=True)
        if self.failedTries == self.maxTries:
            print()
            print('   _________')
            print('   | /     |')
            print('   |/     (_)')
            print('   |      /|\\ ')
            print('   |       |')
            print('   |      / \\')
            print('  _|_')
            print(' |   |________')
            print(' |            |')
            print(' |____________|')
